import os
import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlQuery

from .LoginScreen import LoginView
from .model import DataModel
from MainWindow import MainWindow
from database.DataManager import DataManager


class LoginController:
    def __init__(self, data_maestros=None, data_empresa=None):
        # 1. Creamos los DataManager para la base de datos maestros y empresa
        self.db_maestros = data_maestros 
        self.db_empresa = data_empresa 

        # 2. El DataModel (SQLite de config) sigue igual
        self.model = DataModel()

        # 3. Vista
        self.view = LoginView(self)

        # 4. Rellenar empresas
        lista = self.model.get_empresas_list()
        self.view.combo_empresa.clear()
        self.view.combo_empresa.addItems(lista)
        self.view.show()

    def handle_login(self):
        datos = self.view.get_credentials()
        resultado = self.model.validar_acceso(datos['empresa'], datos['usuario'], datos['pass'])

        if resultado["success"]:
            session_data = {
                "id_empresa": self.model.get_empresa_id(datos['empresa']),
                "empresa": datos['empresa'],
                "usuario": datos['usuario'],
                "rol": resultado["rol"],
                "ejercicio": "2026",
                "idioma": "es",
                "pais": "España"
            }

            # Verificamos si la BD de la empresa (Postgres/MariaDB) responde
            existe_bd, db_config, error_msg = self.verificar_existencia_bd_empresa(session_data['id_empresa'])

            if existe_bd:
                self.abrir_sistema_principal(session_data, db_config)
            else:
                msg_box = QMessageBox(self.view)
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setWindowTitle("Base de Datos No Disponible")
                msg_box.setText(f"⚠️ No se puede acceder a la base de datos\n\n{error_msg}")
                msg_box.exec()
                self.view.agregar_boton_admin()
        else:
            msg_box = QMessageBox(self.view)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error de Acceso")
            msg_box.setText(resultado["error"])
            msg_box.exec()

    def verificar_existencia_bd_empresa(self, id_empresa):
        """
        Verifica si la base de datos de la empresa existe.
        Ahora usa el DataManager universal para evitar duplicar drivers.
        """
        try:
            db_config = self.model.get_empresa_db_config(id_empresa)
            if not db_config:
                return False, None, "Configuración no encontrada en SQLite local."

            # Mapeo de motor a driver de Qt
            motor_str = db_config.get('motor', 'mariadb').lower()
            motor_qt = "QPSQL" if motor_str == 'postgresql' else "QMARIADB"
            if motor_str == 'mysql': motor_qt = "QMYSQL"

            # Intentamos conectar usando el DataManager (conexión temporal)
            tester = DataManager("temp_verify")
            if not tester.conectar(motor_qt, db_config):
                return False, db_config, tester.db.lastError().text()

            # Verificamos si hay tablas (Postgres usa el esquema 'public')
            query = QSqlQuery(tester.db)
            if motor_qt == "QPSQL":
                sql = "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public'"
            else:
                sql = "SHOW TABLES"

            num_tables = 0
            if query.exec(sql):
                if motor_qt == "QPSQL" and query.next():
                    num_tables = query.value(0)
                else:
                    while query.next(): num_tables += 1

            tester.db.close()
            QSqlDatabase.removeDatabase("temp_verify")

            if num_tables == 0:
                return False, db_config, "La base de datos está vacía (sin tablas)."

            return True, db_config, None

        except Exception as e:
            return False, None, str(e)

    def abrir_sistema_principal(self, session_data, db_config):
        self.view.hide()

        # Conectamos el DataManager principal al motor de la empresa
        motor_str = db_config.get('motor', 'mariadb').lower()
        motor_qt = "QPSQL" if motor_str == 'postgresql' else "QMARIADB"

        self.db_empresa.conectar(motor_qt, db_config)
        self.db_maestros.conectar(motor_qt, db_config)

        self.main_window = MainWindow(
            db_maestros=self.db_maestros,
            db_empresa=self.db_empresa,
            sqlite_model=self.model,
            session_data=session_data,
            modo_rescate=False
        )
        self.main_window.show()
        self.view.deleteLater()

    def handle_admin(self):
        self.view.hide()

        session_data = {
            "id_empresa": 0,
            "empresa": "MODO ADMIN",
            "usuario": "admin",
            "rol": "Administrador",
            "ejercicio": "2026",
            "idioma": "es",
            "pais": "España"
        }

        # 2. Intentamos obtener la configuración de la primera empresa para el modo rescate
        db_config = None
        try:
            empresas_list = self.model.get_empresas_list()
            if empresas_list:
                # Obtenemos el ID y la config de la primera empresa de la lista
                primer_id_empresa = self.model.get_empresa_id(empresas_list[0])
                db_config = self.model.get_empresa_db_config(primer_id_empresa)
                session_data["id_empresa"] = primer_id_empresa

                # Si hay config, intentamos conectar los DataManager
                if db_config:
                    motor_str = db_config.get('motor', 'mariadb').lower()
                    motor_qt = "QPSQL" if motor_str == 'postgresql' else "QMARIADB"
                    if self.db_empresa:
                        self.db_empresa.conectar(motor_qt, db_config)
                    if self.db_maestros:
                        self.db_maestros.conectar(motor_qt, db_config)

        except Exception as e:
            print(f"Error obteniendo configuración en modo admin: {e}")

        # 3. Iniciamos MainWindow en modo_rescate=True
        # Le pasamos db_maestros y db_empresa (que pueden estar conectados o no)
        self.main_window = MainWindow(
            db_maestros=self.db_maestros,
            db_empresa=self.db_empresa,
            sqlite_model=self.model,
            session_data=session_data,
            modo_rescate=True
        )

        self.main_window.show()
        self.view.deleteLater()