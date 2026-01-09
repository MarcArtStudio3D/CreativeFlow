import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from .LoginScreen import LoginView
from .model import DataModel
from MainWindow import MainWindow


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

            if self.comprobar_conexion_bd_empresa(session_data['id_empresa']):
                self.abrir_sistema_principal(session_data)
            else:
                # Si falla la BD de la empresa, permitimos el botón de rescate
                self.view.agregar_boton_admin()
        else:
            # Sustituimos AlertaPersonalizada por QMessageBox nativo o el tuyo
            QMessageBox.critical(self.view, "Error de Acceso", resultado["error"])

    def comprobar_conexion_bd_empresa(self, id_empresa):
        try:
            conn = self.model.get_empresa(id_empresa)
            if conn:
                conn.close()
                return True
            else:
                QMessageBox.warning(self.view, "Error de Conexión",
                                    "No se pudo conectar con la base de datos de la empresa.")
                return False
        except Exception as e:
            print(f"Error de conexión a la base de datos: {e}")
            return False

    def abrir_sistema_principal(self, session_data):
        # En Qt6, ocultamos el login y abrimos la principal
        self.view.hide()

        # Creamos la instancia de la MainWindow (PySide6)
        # Pasamos el model para que la principal tenga acceso al gestor de DB
        self.main_window = MainWindow(self.model, session_data)
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
        # Iniciamos Main en modo rescate
        self.main_window = MainWindow(self.model, session_data, modo_rescate=True)
        self.main_window.show()
        self.view.deleteLater()


# --- EL ARRANQUE DE LA APP ---
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Aplicar un estilo global básico (Opcional, similar al dark mode de ctk)
    app.setStyle("Fusion")

    controller = LoginController()
    sys.exit(app.exec())