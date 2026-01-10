import os
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QPushButton, QFrame, QSizePolicy, QToolButton)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize
from colores import *
from modulos.empresas.controller.controller import EmpresaController
from modulos.empresas.model.model import EmpresaModel
from modulos.empresas.view.EmpresaConfigView import EmpresaConfigView

# Detección de rutas
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(CURRENT_DIR, "images", "modules")

class MainWindow(QMainWindow):
    def __init__(self, data_manager, session_data, sqlite_model=None, modo_rescate=False):
        super().__init__()
        self.data_manager = data_manager  # Para MariaDB (datos operativos)
        self.sqlite_model = sqlite_model  # Para SQLite (configuración de empresas)
        self.session_data = session_data

        # No creamos módulos en el inicio - se crearán bajo demanda
        # Esto ahorra memoria en aplicaciones grandes

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
        """
        Modo rescate: Se activa cuando la BD de la empresa no existe o no está accesible.
        Muestra un banner de advertencia y el sidebar de admin para que el usuario elija qué hacer.
        """
        # Banner de advertencia en el header
        self.lbl_empresa.setStyleSheet("color: #E74C3C; font-weight: bold;")
        self.lbl_rol.setStyleSheet("color: #E74C3C; font-weight: bold;")

        # Banner de advertencia en el content area
        banner_rescate = QFrame()
        banner_rescate.setFixedHeight(80)
        banner_rescate.setStyleSheet(f"background-color: #E74C3C; border-radius: 5px;")
        banner_layout = QVBoxLayout(banner_rescate)

        lbl_rescate = QLabel("⚠️ MODO ADMIN - BASE DE DATOS NO DISPONIBLE")
        lbl_rescate.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        lbl_rescate.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lbl_instruccion = QLabel("Seleccione un módulo del menú lateral para continuar")
        lbl_instruccion.setStyleSheet("color: white; font-size: 12px;")
        lbl_instruccion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        banner_layout.addWidget(lbl_rescate)
        banner_layout.addWidget(lbl_instruccion)

        self.content_layout.addWidget(banner_rescate)
        self.content_layout.addStretch()

        # Sidebar de admin - el usuario elige qué módulo cargar
        self.init_sidebar_admin()

    def init_sidebar(self):
        self.agregar_logo_sidebar()
        modulos = [
            ("PROYECTOS", "proyectos.png"),
            ("VENTAS", "ventas.png"),
            ("COMPRAS", "compras.png"),
            ("ALMACÉN", "almacen.png"),
            ("CONTABILIDAD", "contabilidad.png"),
            ("ESTADÍSTICAS", "estadisticas.png"),
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

        # Limpiar completamente el área de contenido - ELIMINAR widgets de memoria
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()  # Eliminar completamente de memoria

        if nombre_modulo == "EMPRESAS":
            # Siempre recrear el módulo desde cero
            vista_empresas = EmpresaConfigView()
            modelo_empresas = EmpresaModel(self.sqlite_model)
            controlador_empresas = EmpresaController(
                vista_empresas,
                modelo_empresas,
                self.session_data.get('id_empresa')
            )

            self.content_layout.addWidget(vista_empresas)
            vista_empresas.show()

        # Aquí se pueden agregar más módulos cuando estén implementados
        # elif nombre_modulo == "USUARIOS":
        #     vista_usuarios = UsuariosView()
        #     modelo_usuarios = UsuariosModel(self.sqlite_model)
        #     controlador_usuarios = UsuariosController(vista_usuarios, modelo_usuarios)
        #     self.content_layout.addWidget(vista_usuarios)
        #
        # elif nombre_modulo == "VENTAS":
        #     vista_ventas = VentasView()
        #     modelo_ventas = VentasModel(self.data_manager)
        #     controlador_ventas = VentasController(vista_ventas, modelo_ventas)
        #     self.content_layout.addWidget(vista_ventas)

        else:
            # Mensaje para módulos no implementados
            lbl_placeholder = QLabel(f"Módulo '{nombre_modulo}' en desarrollo")
            lbl_placeholder.setStyleSheet("color: #999; font-size: 16px;")
            lbl_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.content_layout.addWidget(lbl_placeholder)
            self.content_layout.addStretch()
