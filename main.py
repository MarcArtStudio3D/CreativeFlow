import os
import sys

from PySide6.QtCore import QTranslator, QLocale
from PySide6.QtWidgets import QApplication
from helpers.messagebox_styles import MessageBoxStyler


def aplicar_estilo_personalizado(app):

    style_path = "styles.qss"
    if not os.path.exists(style_path):
        print(f"⚠ No se encontró el archivo {style_path}")
        return

    try:
        with open(style_path, "r", encoding="utf-8") as f:
            qss = f.read()

        # Aplicar directamente al QApplication
        app.setStyleSheet(qss)
        print(f"✓ Estilos cargados desde {style_path} (Creative ERP)")
        print(f"✓ Total caracteres QSS: {len(qss)}")

    except Exception as e:
        print(f"❌ Error cargando estilos: {e}")

def main():
    # Suprimir warnings de drivers SQL que no afectan la funcionalidad
    os.environ["QT_LOGGING_RULES"] = "qt.sql.qsqldatabase.warning=false"

    app = QApplication(sys.argv)



    # Cargar traductor
    translator = QTranslator()
    # Supongamos que tus archivos se llaman 'app_fr.qm', 'app_ca.qm'...
    idioma = QLocale.system().name()  # Detecta si es fr_FR, ca_ES, es_ES...
    if translator.load(f"translations/app_{idioma}.qm"):
        app.installTranslator(translator)

    app.setApplicationName("Creative Flow - Projects Pipeline System")

    # Aplicar el QSS de Creative ERP
    aplicar_estilo_personalizado(app)

    # Instalar el interceptor global de QMessageBox para aplicar estilos automáticamente
    messagebox_styler = MessageBoxStyler()
    app.installEventFilter(messagebox_styler)
    print("✓ Estilos automáticos de QMessageBox activados")

    # Iniciar controlador
    from login.controller import LoginController
    login_ctrl = LoginController()

    login_ctrl.view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

