
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QTableView, QComboBox, QLabel, QHBoxLayout, QPushButton
from PySide6.QtSql import QSqlQueryModel, QSqlQuery
from PySide6.QtCore import Qt, Signal


class DBConsultaView(QDialog):
    # Definimos una señal que devuelva el registro seleccionado (como tu _r en C++)
    registro_seleccionado = Signal(object)

    def __init__(self, db_conexion, parent=None):
        super().__init__(parent)
        self.db = db_conexion
        self.sql_base = ""
        self.sql_filtrada = ""
        self.id_seleccionado = None
        self.registro = None
        self.headers = []  # Inicializar headers

        self.setup_ui()
        self.modelo = QSqlQueryModel(self)

    def setup_ui(self):
        self.setWindowTitle("Buscar...")
        self.resize(800, 600)
        layout = QVBoxLayout(self)

        # Filtros superiores (Como en tu C++)
        filtros_layout = QHBoxLayout()
        self.lbl_tabla = QLabel("Tabla")
        self.cmb_campo = QComboBox()
        self.txt_buscar = QLineEdit()
        self.txt_buscar.setPlaceholderText("Escribe para filtrar...")
        self.cmb_sentido = QComboBox()
        self.cmb_sentido.addItems(["A-Z", "Z-A"])

        filtros_layout.addWidget(self.lbl_tabla)
        filtros_layout.addWidget(self.cmb_campo)
        filtros_layout.addWidget(self.txt_buscar)
        filtros_layout.addWidget(self.cmb_sentido)
        layout.addLayout(filtros_layout)

        # La Tabla
        self.tabla = QTableView()
        self.tabla.setSelectionBehavior(QTableView.SelectRows)
        self.tabla.setEditTriggers(QTableView.NoEditTriggers)
        self.tabla.doubleClicked.connect(self.aceptar)
        layout.addWidget(self.tabla)

        # Botones
        btns = QHBoxLayout()
        self.btn_aceptar = QPushButton("Aceptar")
        self.btn_aceptar.clicked.connect(self.aceptar)
        btns.addStretch()
        btns.addWidget(self.btn_aceptar)
        layout.addLayout(btns)

        # Eventos (textChanged como en C++)
        self.txt_buscar.textChanged.connect(self.ejecutar_filtro)
        self.cmb_sentido.currentIndexChanged.connect(self.ejecutar_filtro)
        self.cmb_campo.currentIndexChanged.connect(self.ejecutar_filtro)

    def set_config(self, titulo, sql_base, campos_busqueda, headers):
        self.setWindowTitle(titulo)
        self.sql_base = sql_base
        self.cmb_campo.clear()
        self.cmb_campo.addItems(campos_busqueda)
        self.headers = headers
        # No ejecutamos el filtro aquí todavía,
        # mejor esperar a tener los tamaños si se van a definir
        self.ejecutar_filtro()
        self.txt_buscar.setFocus()

    def ejecutar_filtro(self):
        texto = self.txt_buscar.text()
        campo = self.cmb_campo.currentText()
        sentido = "DESC" if self.cmb_sentido.currentText() == "Z-A" else "ASC"

        # 1. Construcción del SQL
        connector = " AND " if "WHERE" in self.sql_base.upper() else " WHERE "
        # Usamos f-strings pero con cuidado
        filtro = f"{connector} {campo} LIKE '%{texto}%'"
        self.sql_filtrada = f"{self.sql_base} {filtro} ORDER BY {campo} {sentido}"

        # 2. EL CAMBIO CLAVE: Usar el modelo de Qt, no fetchall()
        # Importante: self.db debe ser la instancia de QSqlDatabase que ya tienes
        query = QSqlQuery(self.db)
        if query.exec(self.sql_filtrada):
            self.modelo.setQuery(query)
            self.tabla.setModel(self.modelo)

            # Ocultar ID y poner headers
            self.tabla.setColumnHidden(0, True)
            for i, h in enumerate(self.headers):
                self.modelo.setHeaderData(i, Qt.Horizontal, h)
            self.tabla.horizontalHeader().setStretchLastSection(True)
        else:
            print(f"Error SQL: {query.lastError().text()}")

    def set_tamano_columnas(self, lista_tamanos):
        """
        Recibe una lista de enteros con los píxeles.
        Ejemplo: [0, 300, 100] (el primero es el ID oculto)
        """
        header = self.tabla.horizontalHeader()
        for i, tamano in enumerate(lista_tamanos):
            if i < self.modelo.columnCount():
                self.tabla.setColumnWidth(i, tamano)

    def aceptar(self):
        idx = self.tabla.currentIndex()
        if idx.isValid():
            row = idx.row()
            self.id_seleccionado = self.modelo.record(row).value(0)
            self.registro = self.modelo.record(row)
            self.accept()