# modulos/configuracion/view/EmpresaConfigView.py
from PySide6.QtWidgets import QDialog
from .ui_frmempresas import Ui_FrmEmpresas


class EmpresaConfigView(QDialog, Ui_FrmEmpresas):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
