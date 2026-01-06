import customtkinter as ctk
from colores import *


class VentasModule(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        # Submenú superior (Navegación de Ventas)
        self.submenu = ctk.CTkFrame(self, fg_color="transparent", height=40)
        self.submenu.pack(fill="x", pady=(0, 10))

        # Diccionario: Nombre de sección -> Nombre del archivo/clase
        self.secciones = {
            "Clientes": "clientes",
            "Artículos": "articulos",
            "Presupuestos": "presupuestos",
            "Facturas": "facturas"
        }

        for nombre in self.secciones.keys():
            btn = ctk.CTkButton(
                self.submenu, text=nombre, width=100,
                command=lambda n=nombre: self.cargar_subvista(n),
                fg_color="transparent", text_color="#888888", hover_color="#333333"
            )
            btn.pack(side="left", padx=2)

        # Contenedor donde se dibuja la sub-pantalla
        self.container = ctk.CTkFrame(self, fg_color="#2D2D2D", corner_radius=15)
        self.container.pack(fill="both", expand=True)

        # Cargar Clientes por defecto
        self.cargar_subvista("Clientes")

    def cargar_subvista(self, nombre):
        # Limpiar contenedor
        for w in self.container.winfo_children():
            w.destroy()

        # Aquí es donde ocurre la magia RAD:
        # En lugar de 20 IFs, podemos intentar importar dinámicamente
        if nombre == "Clientes":
            from modulos.ventas_vistas.clientes import ClientesView
            view = ClientesView(self.container)
            view.pack(fill="both", expand=True, padx=20, pady=20)