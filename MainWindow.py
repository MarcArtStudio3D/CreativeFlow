import os
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QPushButton, QFrame, QSizePolicy, QToolButton)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize
from colores import *

# Detección de rutas
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(CURRENT_DIR, "images", "modules")

class MainWindow(QMainWindow):
    def __init__(self, data_manager, session_data, modo_rescate=False):
        super().__init__()
        self.data_manager = data_manager
        self.session_data = session_data

        self.setWindowTitle("CREATIVE FLOW")
        self.showMaximized()

        # Icono de ventana
        self.ruta_icono = os.path.join(IMAGES_DIR, "LogoIcono.png")
        if os.path.exists(self.ruta_icono):
            self.setWindowIcon(QIcon(self.ruta_icono))

        # --- ESTRUCTURA PRINCIPAL ---
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # 1. HEADER
        self.setup_header()

        # 2. CUERPO (Sidebar + Contenido)
        self.body_layout = QHBoxLayout()
        self.body_layout.setSpacing(0)
        self.main_layout.addLayout(self.body_layout)

        # 3. SIDEBAR
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(130)
        self.sidebar.setStyleSheet(f"background-color: {COLOR_FONDO_CONTENEDORES}; border-right: 1px solid {COLOR_LINEAS};")
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setAlignment(Qt.AlignTop)
        self.body_layout.addWidget(self.sidebar)

        # 4. ÁREA DE CONTENIDO
        self.content_area = QFrame()
        self.content_area.setStyleSheet(f"background-color: {COLOR_FONDO_PRINCIPAL};")
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(20, 20, 20, 20)
        self.body_layout.addWidget(self.content_area, stretch=1)

        # Lógica de inicio según modo
        if modo_rescate:
            self.setup_modo_rescate()
        else:
            self.init_sidebar()

    def setup_header(self):
        self.header = QFrame()
        self.header.setFixedHeight(40)
        self.header.setStyleSheet(f"background-color: {COLOR_FONDO_CONTENEDORES}; border-bottom: 1px solid {COLOR_LINEAS};")
        layout = QHBoxLayout(self.header)
        layout.setContentsMargins(20, 0, 20, 0)

        self.lbl_empresa = self.crear_label_header(f"EMPRESA: {self.session_data['empresa']}")
        self.lbl_user = self.crear_label_header(f"USUARIO: {self.session_data['usuario']}")
        self.lbl_rol = self.crear_label_header(f"ROL: {self.session_data['rol']}")
        self.lbl_year = self.crear_label_header(f"EJERCICIO: {self.session_data['ejercicio']}")

        layout.addWidget(self.lbl_empresa)
        layout.addStretch()
        layout.addWidget(self.lbl_user)
        layout.addSpacing(20)
        layout.addWidget(self.lbl_rol)
        layout.addSpacing(20)
        layout.addWidget(self.lbl_year)
        self.main_layout.addWidget(self.header)

    def setup_modo_rescate(self):
        # Restauramos el mensaje visual de error de BD
        lbl_rescate = QLabel("MODO ADMIN ACTIVADO\n(Error de conexión con la BD de la empresa)")
        lbl_rescate.setStyleSheet(f"color: #E74C3C; font-size: 20px; font-weight: bold;")
        lbl_rescate.setAlignment(Qt.AlignCenter)
        self.content_layout.addStretch()
        self.content_layout.addWidget(lbl_rescate)
        self.content_layout.addStretch()
        self.init_sidebar_admin()

    def init_sidebar(self):
        self.agregar_logo_sidebar()
        modulos = [
            ("PROYECTOS", "proyectos.png"), ("VENTAS", "ventas.png"),
            ("COMPRAS", "compras.png"), ("ALMACÉN", "almacen.png"),
            ("CONTABILIDAD", "contabilidad.png"), ("ESTADÍSTICAS", "estadisticas.png"),
            ("ADMINISTRACIÓN", "configuracion.png")
        ]
        for nombre, icono in modulos:
            self.crear_tarjeta_modulo(nombre, icono)
        self.sidebar_layout.addStretch()

    def init_sidebar_admin(self):
        self.agregar_logo_sidebar()
        modulos = [
            ("USUARIOS", "usuarios.png"), ("EMPRESAS", "empresas.png"),
            ("ROLES", "roles.png"), ("BACKUPS", "backups.png"),
            ("CONFIGURACIÓN", "configuracion.png")
        ]
        for nombre, icono in modulos:
            self.crear_tarjeta_modulo(nombre, icono)
        self.sidebar_layout.addStretch()

    def agregar_logo_sidebar(self):
        lbl_logo = QLabel("CREATIVE FLOW")
        lbl_logo.setStyleSheet(f"color: {COLOR_NARANJA}; font-size: 14px; font-weight: bold; margin: 20px 0; border: none;")
        lbl_logo.setAlignment(Qt.AlignCenter)
        self.sidebar_layout.addWidget(lbl_logo)

    def crear_tarjeta_modulo(self, nombre, nombre_archivo):
        btn = QToolButton()
        btn.setText(nombre.capitalize())
        btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        btn.setFixedHeight(95)

        ruta_img = os.path.join(IMAGES_DIR, nombre_archivo)
        if os.path.exists(ruta_img):
            btn.setIcon(QIcon(ruta_img))
            btn.setIconSize(QSize(55, 55))

        btn.setStyleSheet(f"""
            QToolButton {{
                background-color: transparent;
                color: {COLOR_TEXTO_ETIQUETAS};
                border: none;
                border-radius: 12px;
                font-weight: bold;
                font-size: 10px;
                padding: 10px;
            }}
            QToolButton:hover {{ background-color: {COLOR_FONDO_COMBOS}; }}
        """)

        # Mapeo de nombres para el comparador del controlador
        id_modulo = "EMPRESAS" if nombre in ["ADMINISTRACIÓN", "CONFIGURACIÓN"] else nombre
        btn.clicked.connect(lambda: self.cambiar_modulo(id_modulo))
        self.sidebar_layout.addWidget(btn)

    def crear_label_header(self, texto):
        lbl = QLabel(texto)
        lbl.setStyleSheet(f"color: {COLOR_GRIS_TECNICO}; font-size: 11px; font-weight: bold; border: none;")
        return lbl

    def cambiar_modulo(self, nombre_modulo):
        print(f"DEBUG: Cargando {nombre_modulo}")
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            if item.widget(): item.widget().deleteLater()

        if nombre_modulo == "EMPRESAS":
            try:
                from modulos.configuracion.view.EmpresaConfigView import EmpresaConfigView
                from modulos.configuracion.model.modelo import EmpresaModel
                from modulos.configuracion.controller.EmpresaController import EmpresaController

                self.modelo_actual = EmpresaModel(self.data_manager)
                self.vista_actual = EmpresaConfigView()
                self.controlador_actual = EmpresaController(
                    self.vista_actual, self.modelo_actual, self.session_data.get('id_empresa')
                )
                self.content_layout.addWidget(self.vista_actual)
                self.vista_actual.show()
            except Exception as e:
                print(f"Error al cargar Empresas: {e}")