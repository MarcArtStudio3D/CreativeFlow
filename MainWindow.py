import os
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QPushButton, QFrame, QSizePolicy, QToolButton, QGridLayout)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize
from colores import *
from modulos.empresas.controller.controller import EmpresaController
from modulos.empresas.model.model import EmpresaModel
from modulos.empresas.view.EmpresaConfigView import EmpresaConfigView

from modulos.ventas.controller import ClientesController
from modulos.ventas.model import ClientesModel
from modulos.ventas.view import clientes_view


# Detección de rutas
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(CURRENT_DIR, "images", "modules")

class MainWindow(QMainWindow):
    def __init__(self, db_maestros, db_empresa, session_data, sqlite_model=None, modo_rescate=False):
        super().__init__()
        self.db_maestros = db_maestros  # Para MariaDB/PostgreSQL (datos maestros)
        self.db_empresa = db_empresa  # Para MariaDB/PostgreSQL (datos empresa)
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
        # NO aplicar setStyleSheet aquí - bloquea la herencia del QSS global
        # El color de fondo vendrá del QSS global o QPalette
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
 
    def cambiar_modulo(self, nombre_modulo, view_class=None):
        print(f"DEBUG: Cargando {nombre_modulo}")

        # 1. LIMPIEZA (Tu código original, no se toca)
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # 2. CARGA DINÁMICA (Para las 80+ pantallas futuras)
        # Si pasamos una clase, la montamos automáticamente y salimos
        if view_class:
            instancia = view_class()
            if hasattr(instancia, 'set_db'):
                instancia.set_db(self.db_empresa, self.db_maestros, self.session_data)

            self.content_layout.addWidget(instancia)
            self.content_layout.setContentsMargins(0, 0, 0, 0)
            return instancia

        # 3. LÓGICA DE MENÚS Y CASOS ESPECIALES (Tu código original)
        if nombre_modulo == "EMPRESAS":
            self.vista_empresas = EmpresaConfigView()
            modelo_empresas = EmpresaModel(self.sqlite_model)
            self.controlador_empresas = EmpresaController(
                self.vista_empresas, modelo_empresas, self.session_data,
                db_maestros=self.db_maestros,
                db_empresa=self.db_empresa
            )
            self.content_layout.addWidget(self.vista_empresas)


        elif nombre_modulo == "VENTAS":

            # Ahora pasamos también el nombre del icono

            modulos_ventas = [

                ("CLIENTES", self.abrir_gestion_clientes, "clientes.png"),

                ("PRESUPUESTOS", None, "ventas.png"),

                ("ALBARANES", None, "ventas.png"),

                ("FACTURAS", None, "ventas.png"),

                ("ARTÍCULOS", None, "ventas.png"),

            ]

            self.crear_menu_botones("GESTIÓN DE VENTAS", modulos_ventas)

        else:
            # Tu label de "en desarrollo"
            lbl_placeholder = QLabel(f"Módulo '{nombre_modulo}' en desarrollo")
            lbl_placeholder.setStyleSheet("color: #999; font-size: 16px;")
            lbl_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.content_layout.addWidget(lbl_placeholder)
            self.content_layout.addStretch()

    def crear_menu_botones(self, titulo, lista_modulos):
        """
            titulo: Str
            lista_modulos: [(texto, funcion, nombre_archivo_icono), ...]
            """
        container = QWidget()
        layout_principal = QVBoxLayout(container)
        layout_principal.setContentsMargins(40, 30, 40, 30)
        layout_principal.setSpacing(25)

        # Encabezado dinámico
        layout_principal.addWidget(self.crear_label_header(titulo))

        # Grid para las tarjetas
        grid = QGridLayout()
        grid.setSpacing(20)
        grid.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        columnas_max = 5  # Ajusta según el ancho de tu pantalla

        for i, (texto, funcion, icono) in enumerate(lista_modulos):
            # El botón es el contenedor de la tarjeta
            card = QPushButton()
            card.setFixedSize(180, 180)
            card.setCursor(Qt.PointingHandCursor)

            # Layout interno de la tarjeta
            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(15, 20, 15, 15)
            card_layout.setSpacing(10)
            card_layout.addStretch(1)
            # Icono
            lbl_icono = QLabel()
            path_icono = f"images/modules/{icono}"
            if os.path.exists(path_icono):
                pixmap = QPixmap(path_icono).scaled(70, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                lbl_icono.setPixmap(pixmap)
            lbl_icono.setAlignment(Qt.AlignCenter)
            lbl_icono.setStyleSheet("background: transparent; border: none;")

            # Texto
            lbl_texto = QLabel(texto)
            lbl_texto.setAlignment(Qt.AlignCenter)
            lbl_texto.setWordWrap(True)
            lbl_texto.setStyleSheet(
                "color: white; font-weight: bold; font-size: 14px; background: transparent; border: none;")

            card_layout.addWidget(lbl_icono)
            card_layout.addWidget(lbl_texto)
            card_layout.addStretch(1)

            # Estilo QSS para la tarjeta (Moderno y oscuro)
            card.setStyleSheet(f"""
                    QPushButton {{
                        background-color: #1e1e1e;
                        border: 1px solid #333;
                        border-radius: 12px;
                    }}
                    QPushButton:hover {{
                        background-color: #2a2a2a;
                        border: 2px solid {COLOR_NARANJA};
                    }}
                    QPushButton:pressed {{
                        background-color: #111;
                    }}
                """)

            if funcion:
                card.clicked.connect(funcion)

            fila = i // columnas_max
            columna = i % columnas_max
            grid.addWidget(card, fila, columna)

        layout_principal.addLayout(grid)
        layout_principal.addStretch()  # Empuja todo hacia arriba

        self.content_layout.addWidget(container)

    def abrir_gestion_clientes(self):
        from modulos.ventas.view.clientes_view import ClientesView  # Cambia por el nombre de tu archivo

        self.vista_clientes_detalle = self.cambiar_modulo("CLIENTES", view_class=ClientesView)