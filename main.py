import os
import sys
from PySide6.QtCore import Qt, QTranslator, QLocale
from PySide6.QtWidgets import QApplication


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

    # Iniciar controlador
    from login.controller import LoginController
    login_ctrl = LoginController()

    login_ctrl.view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

