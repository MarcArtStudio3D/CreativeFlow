# main.py
from login.controller import LoginController

def main():
    # Iniciamos el controlador del Login
    # Él se encargará de levantar la vista y conectar con el modelo
    app = LoginController()

if __name__ == "__main__":
    main()