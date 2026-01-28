import os
import sys
from PySide6.QtCore import QTranslator, QLocale, QCoreApplication
from PySide6.QtWidgets import QApplication
from helpers.messagebox_styles import MessageBoxStyler
# Importamos el nuevo DataManager (asumiendo que está en database/manager.py)
from database.DataManager import DataManager


def aplicar_estilo_personalizado(app):
    style_path = "styles.qss"
    if os.path.exists(style_path):
        with open(style_path, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
        print(f"✓ Estilos cargados desde {style_path}")


def main():
    # 1. Ajustes específicos para Arch Linux y Qt
    os.environ["QT_LOGGING_RULES"] = "qt.sql.qsqldatabase.warning=false"
    # Forzamos la ruta de plugins por si acaso en Arch
    QCoreApplication.addLibraryPath("/usr/lib/qt6/plugins")

    app = QApplication(sys.argv)

    # 2. Inicializar DataManager Global (SIN conectar aún)
    # Este objeto vivirá durante toda la sesión
    db_maestros = DataManager(connection_name="conn_maestros")
    db_empresa = DataManager(connection_name="conn_empresa")

    # 3. Traducciones y Estilos
    translator = QTranslator()
    idioma = QLocale.system().name()
    if translator.load(f"translations/app_{idioma}.qm"):
        app.installTranslator(translator)

    app.setApplicationName("Creative Flow - Projects Pipeline System")
    aplicar_estilo_personalizado(app)

    # 4. Estilos de Mensajes
    messagebox_styler = MessageBoxStyler()
    app.installEventFilter(messagebox_styler)

    # 5. Iniciar Login pasándole los DataManager
    from login.controller import LoginController

    # IMPORTANTE: Pasamos db_maestros y db_empresa al controlador
    login_ctrl = LoginController(data_maestros=db_maestros, data_empresa=db_empresa)

    login_ctrl.view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()