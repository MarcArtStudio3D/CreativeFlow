import os
import sys
from PySide6.QtWidgets import QApplication
from login.controller import LoginController
from colores import *


def aplicar_estilo_personalizado(app):
    style_path = "styles.qss"
    if not os.path.exists(style_path):
        return

    with open(style_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Extraemos las variables (líneas que empiezan por @)
    # Buscamos patrones como @nombre: #color;
    import re
    variables = re.findall(r"(@\w+):\s*(#?\w+);", content)

    # 2. Limpiamos el contenido quitando las definiciones de variables
    # para que Qt no se confunda al leer el QSS final
    pure_qss = re.sub(r"@\w+:\s*#?\w+;", "", content)

    # 3. Reemplazamos cada variable en el resto del código
    for var_name, var_value in variables:
        pure_qss = pure_qss.replace(var_name, var_value)

    app.setStyleSheet(pure_qss)

def main():
    # 1. Crear la instancia de la aplicación (El motor de Qt)
    app = QApplication(sys.argv)

    # 2. Configurar estilo visual
    app.setStyle("Fusion")

    # 3. Aplicar estilos globales modernos para TODA la aplicación (300+ pantallas)
    aplicar_estilo_personalizado(app)

    # 4. Iniciamos el controlador del Login
    login_ctrl = LoginController()

    # 5. El bucle de eventos principal
    sys.exit(app.exec())


if __name__ == "__main__":
    main()