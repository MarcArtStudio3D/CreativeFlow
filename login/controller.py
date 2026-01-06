from helpers.componentes import  AlertaPersonalizada

from MainWindow import MainWindow
from .model import DataModel
from .LoginScreen import LoginView


class LoginController:
    def __init__(self):
        self.model = DataModel()
        # Creamos la vista y le pasamos ESTE controlador
        self.view = LoginView(self)

        # Rellenamos el combo al arrancar
        lista = self.model.get_empresas_list()
        self.view.combo_empresa.configure(values=lista)

        self.view.mainloop()

    def handle_login(self):
        datos = self.view.get_credentials()

        # Validar contra SQLite
        resultado = self.model.validar_acceso(
            datos['empresa'],
            datos['usuario'],
            datos['pass']
        )

        if resultado["success"]:
            # Guardamos los datos de la sesión
            session_data = {
                "empresa": datos['empresa'],
                "usuario": datos['usuario'],
                "rol": resultado["rol"],
                "ejercicio": "2026"  # Podrías sacarlo de un campo fecha
            }
            self.abrir_sistema_principal(session_data)
        else:
            AlertaPersonalizada(resultado["error"])

    def abrir_sistema_principal(self, session_data):
        self.view.destroy()  # Cerramos login
        app_principal = MainWindow(session_data)  # Lanzamos Main
        app_principal.mainloop()
if __name__ == "__main__":
    LoginController()