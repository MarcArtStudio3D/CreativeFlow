# main_app/MainWindow.py
from PIL import Image, ImageTk
import os
import customtkinter as ctk
from colores import *

# Esto detecta la carpeta donde está MainWindow.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 1. Detectamos dónde está ESTE archivo (MainWindow.py)
# Si MainWindow.py está en la raíz de CreativeFlow, esto ya es la carpeta del proyecto
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Creamos la ruta completa a la carpeta de imágenes
IMAGES_DIR = os.path.join(CURRENT_DIR, "images", "modules")

class MainWindow(ctk.CTk):
    def __init__(self, session_data, modo_rescate = False):
        super().__init__()
        self.session_data = session_data  # Guardamos los datos de la sesión
        self.title("CREATIVE FLOW")
        #  Maximizar la ventana al iniciar
        try:
            self.attributes('-zoomed', True)  # Funciona en la mayoría de Linux
        except:
            self.state('zoomed')  # Fallback para Windows/MacOS
        # Definir la ruta del icono (usa PNG para mejor compatibilidad en Linux/Mac)
        self.ruta_icono = os.path.join(IMAGES_DIR, "LogoIcono.png")

        if os.path.exists(self.ruta_icono):
            # En Windows suele usarse self.iconbitmap(), pero en Linux esto es más robusto:
            img_icono = Image.open(self.ruta_icono)
            photo = ImageTk.PhotoImage(img_icono)
            self.wm_iconphoto(False, photo)
        else:
            print(f"Aviso: No se encontró el icono en {self.ruta_icono}")

        # Diccionario para guardar las instancias de los módulos (Lazy Loading)
        self.modulos = {}
        # --- BARRA DE ESTADO SUPERIOR (Header) ---
        self.header = ctk.CTkFrame(self, height=40, corner_radius=0, fg_color=COLOR_FONDO_CONTENEDORES)
        self.header.pack(side="top", fill="x")
        # Etiquetas dinámicas usando session_data
        self.lbl_empresa = self.crear_label_header(f"EMPRESA: {session_data['empresa']}")
        self.lbl_user = self.crear_label_header(f"USUARIO: {session_data['usuario']}")
        self.lbl_rol = self.crear_label_header(f"ROL: {session_data['rol']}")
        self.lbl_year = self.crear_label_header(f"EJERCICIO: {session_data['ejercicio']}")

        # Empaquetamos de derecha a izquierda o con espaciado
        self.lbl_empresa.pack(side="left", padx=20)
        self.lbl_year.pack(side="right", padx=20)
        self.lbl_rol.pack(side="right", padx=20)
        self.lbl_user.pack(side="right", padx=20)
        # --- LAYOUT PRINCIPAL ---
        # 1. Sidebar (Izquierda)
        self.sidebar = ctk.CTkFrame(self, width=120, corner_radius=0, fg_color=COLOR_FONDO_CONTENEDORES)
        self.sidebar.pack(side="left", fill="y")

        # 2. Contenedor Derecho (Navegación + Contenido)
        self.main_container = ctk.CTkFrame(self, corner_radius=0, fg_color=COLOR_FONDO_PRINCIPAL)
        self.main_container.pack(side="right", expand=True, fill="both")

        # 3. Área de Contenido Dinámico (donde se cargan los frames)
        self.content_area = ctk.CTkFrame(self.main_container, corner_radius=0, fg_color="transparent")
        self.content_area.pack(expand=True, fill="both", padx=20, pady=20)
        if modo_rescate:
            # Modo Rescate: Mostrar mensaje especial
            lbl_rescate = ctk.CTkLabel(
                self.content_area,
                text="MODO RESCATE ACTIVADO\nContacte con soporte técnico.",
                font=("Arial", 20, "bold"),
                text_color="#E74C3C",
                justify="center"
            )
            lbl_rescate.pack(expand=True)
        else:
            self.init_sidebar()

    def init_sidebar(self):
        # Título o Logo arriba
        self.lbl_logo = ctk.CTkLabel(
            self.sidebar,
            text="CREATIVE FLOW",
            font=("Inter", 16, "bold"),  # Usa una fuente moderna
            text_color=COLOR_NARANJA
        )
        self.lbl_logo.pack(pady=30)  # Dale mucho aire arriba y abajo

        # Definimos los módulos con sus iconos
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

    def crear_tarjeta_modulo(self, nombre, nombre_archivo):
        # Construimos la ruta absoluta: /home/tuuser/CreativeFlow/images/modules/proyectos.png
        ruta_img = os.path.join(IMAGES_DIR, nombre_archivo)

        if os.path.exists(ruta_img):
            img = ctk.CTkImage(
                light_image=Image.open(ruta_img),
                dark_image=Image.open(ruta_img),
                size=(60, 60)
            )
        else:
            print(f"Error: No encuentro la imagen en {ruta_img}")
            img = None

        # La "Tarjeta" es un botón con estilo especial
        btn = ctk.CTkButton(
            self.sidebar,
            text=nombre.capitalize(),
            image=img,
            compound="top",        # Imagen arriba, texto abajo
            command=lambda n=nombre: self.cambiar_modulo(n),
            height=90,             # Más alto para que parezca un cuadrado/tarjeta
            fg_color="transparent",
            hover_color=COLOR_FONDO_COMBOS,  # Un gris un poco más claro que el fondo
            text_color=COLOR_TEXTO_ETIQUETAS,
            font=("Arial", 11, "bold"),
            corner_radius=15,       # Bordes redondeados tipo macOS/Odoo
            border_spacing= 10,   # Espacio entre imagen y texto
        )
        btn.pack(pady=5, padx=10, fill="x")

    def crear_label_header(self, texto):
        return ctk.CTkLabel(
            self.header,
            text=texto,
            font=("Arial", 11, "bold"),
            text_color=COLOR_GRIS_TECNICO
        )

    def cambiar_modulo(self, nombre_modulo):
        # 1. Limpiamos el contenido actual
        for widget in self.content_area.winfo_children():
            widget.destroy()

        # 2. Cargamos el módulo con la sesión de la empresa actual
        if nombre_modulo == "VENTAS":
            from modulos.ventas import VentasModule

            # Le pasamos self.session_data para que sepa qué 'archivo_sqlite' usar
            modulo_ventas = VentasModule(self.content_area, self.session_data)
            modulo_ventas.pack(fill="both", expand=True)

        elif nombre_modulo == "PROYECTOS":
            # Ejemplo para futuros módulos
            pass
