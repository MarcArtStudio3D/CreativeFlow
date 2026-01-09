import sys
from PySide6.QtWidgets import QApplication
from login.controller import LoginController


def main():
    # 1. Crear la instancia de la aplicación (El motor de Qt)
    # Sin esto, cualquier intento de crear un Widget dará error
    app = QApplication(sys.argv)

    # 2. Configurar estilo visual (Opcional pero recomendado para consistencia)
    app.setStyle("Fusion")

    # 3. Iniciamos el controlador del Login
    # Ahora el controlador NO debe llamar a un mainloop interno,
    # simplemente instancia la vista y la muestra (.show())
    login_ctrl = LoginController()

    # 4. El bucle de eventos principal
    # Esta línea mantiene el programa vivo y procesando clics
    sys.exit(app.exec())


if __name__ == "__main__":
    main()