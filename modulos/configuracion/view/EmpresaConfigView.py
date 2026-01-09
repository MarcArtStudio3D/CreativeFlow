import customtkinter as ctk


class EmpresaConfigView(ctk.CTkFrame):
    def __init__(self, master, session_data):
        super().__init__(master, fg_color="transparent")
        self.widgets = {}  # Mapa para el autoguardado

        # 1. BARRA DE PESTAÑAS (Botones pegados)
        self.tab_bar = ctk.CTkFrame(self, fg_color="transparent")
        self.tab_bar.pack(fill="x", padx=20, pady=(10, 0))  # pady inferior 0 para pegar al frame

        # 2. CONTENEDOR PRINCIPAL (El "cuerpo" de la ficha)
        self.container = ctk.CTkFrame(self, border_width=2, border_color="#3b8ed0")
        self.container.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        self.setup_tabs()
        self.show_tab("GENERAL")  # Pestaña por defecto

    def setup_tabs(self):
        # Botones con esquinas redondeadas SOLO arriba (si CTK lo permite) o normales
        # Pero los pegamos uno al lado del otro
        tabs = [
            ("General", "GENERAL"),
            ("Comercial", "COMERCIAL"),
            ("Contabilidad", "CONTA"),
            ("Base de Datos", "DB")
        ]

        self.tab_buttons = {}
        for text, key in tabs:
            btn = ctk.CTkButton(
                self.tab_bar, text=text, width=120, height=35,
                corner_radius=10,  # Esto le da el look de solapa
                command=lambda k=key: self.show_tab(k),
                fg_color="#2b2b2b", hover_color="#3b8ed0"
            )
            btn.pack(side="left", padx=2)
            self.tab_buttons[key] = btn

    def show_tab(self, key):
        # Limpiar contenedor
        for widget in self.container.winfo_children():
            widget.destroy()

        # Resaltar botón activo
        for k, btn in self.tab_buttons.items():
            btn.configure(fg_color="#3b8ed0" if k == key else "#2b2b2b")

        # Cargar contenido
        if key == "GENERAL":
            self.draw_general()
        elif key == "CONTA":
            self.draw_contabilidad()

    def crear_campo_rad(self, parent, label_text, db_field, column=0):  # <--- Eliminado 'row'
        """
        Crea un par Label-Entry alineado usando pack.
        """
        frame_fila = ctk.CTkFrame(parent, fg_color="transparent")
        frame_fila.pack(fill="x", padx=20, pady=2)  # Pady pequeño para que quepa más

        lbl = ctk.CTkLabel(frame_fila, text=label_text, width=150, anchor="w")
        lbl.pack(side="left")

        ent = ctk.CTkEntry(frame_fila, width=350)
        ent.pack(side="left", padx=(10, 0), fill="x", expand=True)

        self.widgets[db_field] = ent

    def draw_general(self):
        # Contenedor con scroll por si hay muchos campos
        scroll = ctk.CTkScrollableFrame(self.container, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=5, pady=5)

        # --- SECCIÓN: IDENTIFICACIÓN ---
        sec_id = ctk.CTkFrame(scroll, fg_color="#2b2b2b", border_width=1, border_color="#3d3d3d")
        sec_id.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(sec_id, text="  IDENTIFICACIÓN FISCAL", font=("Arial", 13, "bold"), text_color="#3b8ed0").pack(
            anchor="w", pady=10)

        self.crear_campo_rad(sec_id, "Código Empresa:", "codigoempresa")
        self.crear_campo_rad(sec_id, "Nombre Comercial:", "nombre_comercial")
        self.crear_campo_rad(sec_id, "Nombre Fiscal:", "nombre_fiscal")
        self.crear_campo_rad(sec_id, "CIF / SIREN:", "cif_siren")

        # --- SECCIÓN: LOCALIZACIÓN ---
        sec_loc = ctk.CTkFrame(scroll, fg_color="#2b2b2b", border_width=1, border_color="#3d3d3d")
        sec_loc.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(sec_loc, text="  UBICACIÓN Y CONTACTO", font=("Arial", 13, "bold"), text_color="#3b8ed0").pack(
            anchor="w", pady=10)

        self.crear_campo_rad(sec_loc, "Dirección:", "direccion")
        self.crear_campo_rad(sec_loc, "Población:", "poblacion")
        self.crear_campo_rad(sec_loc, "Provincia:", "provincia")
        self.crear_campo_rad(sec_loc, "País:", "pais")