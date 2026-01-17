# modulos/configuracion/view/EmpresaConfigView.py
from PySide6.QtWidgets import QDialog
from .ui_frmClientes import Ui_frmClientes


class ClientesView(QDialog, Ui_frmClientes):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def set_db(self, data_manager):
        """Este es el método que le falta a tu clase"""
        self.db = data_manager
        print("✓ Conexión de base de datos recibida en ClientesView")

        # Una vez que tenemos la DB, podemos cargar los datos
        self.cargar_datos_iniciales()

    def cargar_datos_iniciales(self):
        # Aquí es donde más adelante haremos:
        # self.db.consultar("SELECT * FROM clientes")
        pass