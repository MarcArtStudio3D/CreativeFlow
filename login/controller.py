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
                "ejercicio": "2026"
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
                QMessageBox.warning(
                    self.view,
                    "Base de Datos No Disponible",
                    f"⚠️ No se puede acceder a la base de datos\n\n{error_msg}\n\n"
                    f"Use el botón ADMIN para configurar la base de datos."
                )
                self.view.agregar_boton_admin()
        else:
            # Sustituimos AlertaPersonalizada por QMessageBox nativo o el tuyo
            QMessageBox.critical(self.view, "Error de Acceso", resultado["error"])

    def verificar_existencia_bd_empresa(self, id_empresa):
        """
        Verifica si la base de datos de la empresa existe y es accesible.

        Returns:
            tuple: (existe: bool, db_config: dict or None, error_msg: str or None)
        """
        try:
            # Obtenemos la configuración de la BD desde SQLite
            db_config = self.model.get_empresa_db_config(id_empresa)
            print(f"DEBUG: db_config obtenida: {db_config}")

            if not db_config:
                print("DEBUG: No hay db_config, retornando False")
                return False, None, "No se encontró configuración de base de datos para esta empresa"

            # Intentamos conectar a la base de datos
            import mysql.connector

            motor = db_config.get('motor', 'mariadb').lower()
            print(f"DEBUG: Motor de BD: {motor}")

            if motor == 'postgresql':
                # TODO: Implementar verificación para PostgreSQL
                print("DEBUG: PostgreSQL no implementado, retornando False")
                return False, db_config, "PostgreSQL aún no está implementado"

            # Para MariaDB/MySQL
            try:
                print(f"DEBUG: Intentando conectar a MariaDB: {db_config['host']}:{db_config['port']}/{db_config['database']}")
                conn = mysql.connector.connect(**db_config)
                # Verificamos que la base de datos tiene tablas
                cursor = conn.cursor()
                cursor.execute("SHOW TABLES")
                tables = cursor.fetchall()
                cursor.close()
                conn.close()

                print(f"DEBUG: Conectado exitosamente, tablas encontradas: {len(tables)}")

                if len(tables) == 0:
                    print("DEBUG: Base de datos vacía, retornando False")
                    return False, db_config, f"La base de datos '{db_config['database']}' existe pero está vacía"

                print("DEBUG: BD existe con tablas, retornando True")
                return True, db_config, None

            except mysql.connector.Error as err:
                print(f"DEBUG: Error de MySQL: {err.errno} - {err}")
                if err.errno == 1049:  # Unknown database
                    return False, db_config, f"La base de datos '{db_config['database']}' no existe"
                elif err.errno == 2003:  # Can't connect to MySQL server
                    return False, db_config, f"No se puede conectar al servidor {db_config['host']}:{db_config['port']}"
                elif err.errno == 1045:  # Access denied
                    return False, db_config, f"Acceso denegado para el usuario '{db_config['user']}'"
                else:
                    return False, db_config, f"Error de conexión: {err}"

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
            "usuario": "Administrador",
            "rol": "admin",
            "ejercicio": "2026"
        }

        # En modo admin, intentamos obtener la configuración de la primera empresa disponible
        # o usamos una configuración por defecto
        try:
            empresas_list = self.model.get_empresas_list()
            if empresas_list:
                # Obtenemos el ID de la primera empresa
                primer_id_empresa = self.model.get_empresa_id(empresas_list[0])
                db_config = self.model.get_empresa_db_config(primer_id_empresa)
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