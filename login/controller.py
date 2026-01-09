from operator import truediv

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
            self.id_empresa = self.model.get_empresa_id(datos['empresa'])
            if self.comprobar_conexion_bd_empresa(self.id_empresa):
                self.abrir_sistema_principal(session_data)
            else:
                self.view.agregar_boton_admin()
        else:
            AlertaPersonalizada(resultado["error"])

    def comprobar_conexion_bd_empresa(self, id_empresa):

        try:
            # Intentamos una conexión simple para verificar
            conn = self.model.get_empresa(id_empresa)
            if conn:
                conn.close()
                return True
            else:
                AlertaPersonalizada("Error al conectar con la base de datos de la empresa.", "Error de Conexión")

                return False
        except Exception as e:
            print(f"Error de conexión a la base de datos: {e}")
            return False

    def abrir_sistema_principal(self, session_data):
        self.view.destroy()  # Cerramos login
        app_principal = MainWindow(session_data)  # Lanzamos Main
        app_principal.mainloop()

    def handle_admin(self, session_data):
        self.view.destroy()  # Cerramos login
        app_principal = MainWindow(session_data,True)  # Lanzamos Main
        app_principal.mainloop()

if __name__ == "__main__":
    LoginController()