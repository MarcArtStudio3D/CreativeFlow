# modulos/configuracion/view/EmpresaConfigView.py
from PySide6.QtWidgets import QDialog
from .ui_frmClientes import Ui_frmClientes

class ClientesView(QDialog, Ui_frmClientes):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def set_db(self, data_empresa, data_maestros,session):
        """Este es el método que le falta a tu clase"""
        self.db_empresa = data_empresa
        self.db_maestros = data_maestros

        self.session_data = session
        print("✓ Conexión de base de datos recibida en ClientesView")

        # Ahora que tenemos DB, instanciamos Modelo y Controlador
        from modulos.ventas.model.ClientesModel import ClienteModel
        from modulos.ventas.controller.ClientesController import ClientesController

        self.modelo = ClienteModel(self.db_maestros, self.db_empresa)
        parent_window = self.window()
        # Al crear el controlador, este llamará a cargar_tabla_principal()
        self.controller = ClientesController(self, self.modelo, self.session_data)