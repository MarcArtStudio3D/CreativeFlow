import customtkinter as ctk
from colores import *

class VentasModule(ctk.CTkFrame):
    def __init__(self, master, session_data):
        super().__init__(master, fg_color="transparent")
        self.session = session_data  # Aquí tenemos el 'archivo_sqlite'

        # --- SUB-MENÚ SUPERIOR ---
        self.submenu = ctk.CTkFrame(self, fg_color="transparent", height=40)
        self.submenu.pack(fill="x", pady=(0, 10))

        # Definimos las secciones
        secciones = ["Clientes", "Presupuestos", "Facturas"]
        for sec in secciones:
            btn = ctk.CTkButton(
                self.submenu, text=sec, width=120,
                command=lambda s=sec: self.cargar_subseccion(s),
                fg_color="transparent", text_color=COLOR_TEXTO_ETIQUETAS, hover_color=COLOR_BORDE_NORMAL
            )
            btn.pack(side="left", padx=5)

        # --- CONTENEDOR DINÁMICO ---
        self.view_container = ctk.CTkFrame(self, fg_color=COLOR_FONDO_COMBOS, corner_radius=15)
        self.view_container.pack(fill="both", expand=True)

        self.cargar_subseccion("Clientes")

    def cargar_subseccion(self, nombre):
        for w in self.view_container.winfo_children():
            w.destroy()

        if nombre == "Clientes":
            from modulos.ventas_vistas.clientes import ClientesView
            # Pasamos la sesión a la vista final
            view = ClientesView(self.view_container, self.session)
            view.pack(fill="both", expand=True, padx=20, pady=20)