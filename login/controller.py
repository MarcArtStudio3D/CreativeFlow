import os
import sys
from PySide6.QtWidgets import QApplication, QMessageBox

from .LoginScreen import LoginView
from .model import DataModel
from MainWindow import MainWindow
from database.database import DataManager


class LoginController:
    def __init__(self):
        # 1. El DataModel sigue siendo el mismo (es agnóstico a la UI)
        self.model = DataModel()

        # 2. Creamos la vista
        self.view = LoginView(self)

        # 3. Rellenamos el combo (En Qt es addItems o clear + addItems)
        lista = self.model.get_empresas_list()
        self.view.combo_empresa.clear()
        self.view.combo_empresa.addItems(lista)

        # 4. Mostramos la vista
        self.view.show()

    def handle_login(self):
        datos = self.view.get_credentials()

        # Validar contra SQLite
        resultado = self.model.validar_acceso(
            datos['empresa'],
            datos['usuario'],
            datos['pass']
        )

        if resultado["success"]:
            session_data = {
                "id_empresa": self.model.get_empresa_id(datos['empresa']),
                "empresa": datos['empresa'],
                "usuario": datos['usuario'],
                "rol": resultado["rol"],
                "ejercicio": "2026", # TODO: Obtener del json de configuración de la aplicación
                "idioma": "es", #TODO: Obtener del json de configuración de la aplicación
                "pais": "España" # TODO: Obtener del json de configuración de la aplicación
            }

            # Verificamos si la BD de la empresa existe
            existe_bd, db_config, error_msg = self.verificar_existencia_bd_empresa(session_data['id_empresa'])

            print(f"DEBUG handle_login: existe_bd={existe_bd}, error_msg={error_msg}")

            if existe_bd:
                # Si la BD existe, abrimos el sistema normalmente
                print("DEBUG: Abriendo sistema en modo NORMAL")
                self.abrir_sistema_principal(session_data, db_config)
            else:
                # Si la BD no existe, mostramos el botón de rescate/admin
                print("DEBUG: BD no existe, mostrando botón ADMIN")

                # Crear QMessageBox personalizado con estilo de alerta
                msg_box = QMessageBox(self.view)
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setWindowTitle("Base de Datos No Disponible")
                msg_box.setText(f"⚠️ No se puede acceder a la base de datos\n\n{error_msg}\n\n"
                               f"Use el botón ADMIN para configurar la base de datos.")
                msg_box.exec()
                self.view.agregar_boton_admin()
        else:
            # Crear QMessageBox critical personalizado con fondo rojizo
            msg_box = QMessageBox(self.view)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error de Acceso")
            msg_box.setText(resultado["error"])

            msg_box.exec()

    def verificar_existencia_bd_empresa(self, id_empresa):
        """
        Verifica si la base de datos de la empresa existe y es accesible.
        Usa QSqlDatabase para ser consistente con el resto de la aplicación.

        Returns:
            tuple: (existe: bool, db_config: dict or None, error_msg: str or None)
        """
        from PySide6.QtSql import QSqlDatabase, QSqlQuery
        
        try:
            # Obtenemos la configuración de la BD desde SQLite
            db_config = self.model.get_empresa_db_config(id_empresa)
            print(f"DEBUG: db_config obtenida: {db_config}")

            if not db_config:
                print("DEBUG: No hay db_config, retornando False")
                return False, None, "No se encontró configuración de base de datos para esta empresa"

            motor = db_config.get('motor', 'mariadb').lower()
            print(f"DEBUG: Motor de BD: {motor}")

            # Seleccionar el driver Qt apropiado
            if motor == 'postgresql':
                driver_qt = "QPSQL"
            elif motor in ['mariadb', 'mysql']:
                driver_qt = "QMYSQL"
            else:
                return False, db_config, f"Motor de base de datos '{motor}' no soportado"

            # Crear conexión temporal para verificar
            temp_conn_name = f"verify_db_{id_empresa}"
            if QSqlDatabase.contains(temp_conn_name):
                QSqlDatabase.removeDatabase(temp_conn_name)
            
            temp_db = QSqlDatabase.addDatabase(driver_qt, temp_conn_name)
            temp_db.setHostName(db_config['host'])
            temp_db.setPort(db_config['port'])
            temp_db.setUserName(db_config['user'])
            temp_db.setPassword(db_config['password'])
            temp_db.setDatabaseName(db_config['database'])

            print(f"DEBUG: Intentando conectar a {motor.upper()}: {db_config['host']}:{db_config['port']}/{db_config['database']}")

            # Intentar abrir la conexión
            if not temp_db.open():
                error_text = temp_db.lastError().text()
                print(f"DEBUG: No se pudo abrir la conexión: {error_text}")
                
                # Cerrar y limpiar
                temp_db.close()
                QSqlDatabase.removeDatabase(temp_conn_name)
                
                # Analizar el tipo de error
                if "database" in error_text.lower() and "does not exist" in error_text.lower():
                    return False, db_config, f"La base de datos '{db_config['database']}' no existe"
                elif "authentication" in error_text.lower() or "password" in error_text.lower():
                    return False, db_config, f"Acceso denegado para el usuario '{db_config['user']}'"
                elif "connect" in error_text.lower():
                    return False, db_config, f"No se puede conectar al servidor {db_config['host']}:{db_config['port']}"
                else:
                    return False, db_config, f"Error de conexión: {error_text}"

            # Verificar que la base de datos tiene tablas
            query = QSqlQuery(temp_db)
            
            if motor == 'postgresql':
                # PostgreSQL usa información del esquema público
                sql_check = """
                    SELECT COUNT(*) 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
                """
            else:
                # MariaDB/MySQL
                sql_check = "SHOW TABLES"
            
            if not query.exec(sql_check):
                error_text = query.lastError().text()
                print(f"DEBUG: Error ejecutando query de verificación: {error_text}")
                temp_db.close()
                QSqlDatabase.removeDatabase(temp_conn_name)
                return False, db_config, f"Error consultando tablas: {error_text}"

            # Contar tablas
            num_tables = 0
            if motor == 'postgresql':
                if query.next():
                    num_tables = query.value(0)
            else:
                while query.next():
                    num_tables += 1

            print(f"DEBUG: Conectado exitosamente, tablas encontradas: {num_tables}")

            # Cerrar conexión temporal
            temp_db.close()
            QSqlDatabase.removeDatabase(temp_conn_name)

            if num_tables == 0:
                print("DEBUG: Base de datos vacía, retornando False")
                return False, db_config, f"La base de datos '{db_config['database']}' existe pero está vacía"

            print("DEBUG: BD existe con tablas, retornando True")
            return True, db_config, None


        except Exception as e:
            print(f"DEBUG: Excepción general: {e}")
            return False, None, f"Error verificando base de datos: {str(e)}"

    def abrir_sistema_principal(self, session_data, db_config):
        """
        Abre la ventana principal del sistema en modo normal.
        Solo se llama si la BD ya fue verificada y existe.
        """
        # En Qt6, ocultamos el login y abrimos la principal
        self.view.hide()

        # Creamos el DataManager con la configuración obtenida (para MariaDB)
        data_manager = DataManager(db_config)

        # Creamos la instancia de la MainWindow (PySide6) en MODO NORMAL
        self.main_window = MainWindow(
            data_manager,
            session_data,
            sqlite_model=self.model,
            modo_rescate=False
        )
        self.main_window.show()

        # Liberamos la memoria del login cuando la principal esté lista
        self.view.deleteLater()

    def handle_admin(self):
        self.view.hide()
        session_data = {

                "id_empresa": 0,
                "empresa": "MODO ADMIN",
                "usuario": "admin",
                "rol": "Administrador",
                "ejercicio": "2026", # TODO: Obtener del json de configuración de la aplicación
                "idioma": "es", #TODO: Obtener del json de configuración de la aplicación
                "pais": "France" # TODO: Obtener del json de configuración de la aplicación
        }

        # En modo admin, intentamos obtener la configuración de la primera empresa disponible
        # o usamos una configuración por defecto
        try:
            empresas_list = self.model.get_empresas_list()
            if empresas_list:
                # Obtenemos el ID de la primera empresa
                primer_id_empresa = self.model.get_empresa_id(empresas_list[0])
                db_config = self.model.get_empresa_db_config(primer_id_empresa)
                session_data["id_empresa"] = primer_id_empresa
            else:
                db_config = None
        except Exception as e:
            print(f"Error obteniendo configuración en modo admin: {e}")
            db_config = None

        # Creamos el DataManager (usará configuración por defecto si db_config es None)
        data_manager = DataManager(db_config)

        # Iniciamos Main en modo rescate, pasando también el sqlite_model
        self.main_window = MainWindow(data_manager, session_data, sqlite_model=self.model, modo_rescate=True)
        self.main_window.show()
        self.view.deleteLater()


# --- EL ARRANQUE DE LA APP ---
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Aplicar un estilo global básico (Opcional, similar al dark mode de ctk)
    app.setStyle("Fusion")

    controller = LoginController()
    sys.exit(app.exec())