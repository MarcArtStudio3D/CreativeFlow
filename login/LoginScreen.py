import customtkinter as ctk
from colores import *

class LoginView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title("CREATIVE FLOW - Login")
        self.geometry("500x650")
        self.configure(fg_color=COLOR_NEGRO)  # Fondo negro puro como en la imagen

        # Contenedor central (el recuadro gris oscuro)
        # Contenedor central con tamaño FIJO y anclado al CENTRO
        self.frame = ctk.CTkFrame(
            self,
            fg_color=COLOR_FONDO_CONTENEDORES,
            corner_radius=10,
            border_width=1,
            border_color=COLOR_LINEAS,
            width=400,  # Definimos el ancho fijo
            height=550  # Definimos el alto fijo
        )

        # Al usar place sin 'relwidth' ni 'relheight', el frame no se deforma.
        # 'relx=0.5' y 'rely=0.5' con 'anchor=center' lo mantienen siempre en el medio.
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # IMPORTANTE: Como el frame ahora tiene tamaño fijo,
        # evita que sus hijos lo deformen usando esto:
        self.frame.pack_propagate(False)

        # TÍTULO Y SUBTÍTULO
        self.lbl_titulo = ctk.CTkLabel(self.frame, text="CREATIVE FLOW", text_color=COLOR_NARANJA, font=("Arial Black", 24))
        self.lbl_titulo.pack(pady=(40, 0))

        self.lbl_sub = ctk.CTkLabel(self.frame, text="PROJECTS PIPELINE SYSTEM", text_color=COLOR_GRIS_TECNICO,
                                    font=("Arial", 10, "bold"))
        self.lbl_sub.pack(pady=(0, 30))

        # SELECCIÓN DE EMPRESA (COMBOBOX)
        # Aquí cargaríamos los nombres desde tu SQLite maestra
        self.combo_empresa = ctk.CTkComboBox(self.frame, values=["ARTSTUDIO3D", "OTRA_EMPRESA"],
                                             fg_color=COLOR_LINEAS, border_color=COLOR_BORDE_NORMAL,
                                             button_color=COLOR_BOTONES, height=40)
        self.combo_empresa.pack(padx=30, pady=10, fill="x")

        # USUARIO
        self.lbl_user = ctk.CTkLabel(self.frame, text="USUARIO", font=("Arial", 10, "bold"), text_color=COLOR_FILA_CEBRA)
        self.lbl_user.pack(padx=30, anchor="w")
        self.ent_user = ctk.CTkEntry(self.frame, fg_color=COLOR_FILA_CEBRA, border_color=COLOR_BORDE_NORMAL, height=40)
        self.ent_user.pack(padx=30, pady=(0, 15), fill="x")

        # CONTRASEÑA
        self.lbl_pass = ctk.CTkLabel(self.frame, text="CONTRASEÑA", font=("Arial", 10, "bold"), text_color=COLOR_FILA_CEBRA)
        self.lbl_pass.pack(padx=30, anchor="w")
        self.ent_pass = ctk.CTkEntry(self.frame, fg_color=COLOR_FILA_CEBRA, border_color=COLOR_BORDE_NORMAL, height=40, show="*")
        self.ent_pass.pack(padx=30, pady=(0, 30), fill="x")

        # BOTONES NARANJAS
        self.btn_conectar = ctk.CTkButton(
            self.frame, text="CONECTAR AL PIPELINE",
            fg_color=COLOR_NARANJA,
            hover_color=COLOR_BOTONES_HOVER,
            height=45,
            font=("Arial", 12, "bold"),
            command=self.controller.handle_login)
        self.btn_conectar.pack(padx=30, pady=10, fill="x")
        # 1. Habilitar el foco en el canvas interno
        self.btn_conectar._canvas.configure(takefocus=True, highlightthickness=1, highlightbackground=COLOR_FONDO_INPUTS)

        # 2. Evento: Al recibir el foco (Tab), poner borde blanco
        self.btn_conectar._canvas.bind("<FocusIn>",
                                       lambda e: self.btn_conectar._canvas.configure(highlightcolor=COLOR_BLANCO))

        # 3. Evento: Al perder el foco, volver al color del fondo (ocultarlo)
        self.btn_conectar._canvas.bind("<FocusOut>",
                                       lambda e: self.btn_conectar._canvas.configure(highlightcolor=COLOR_FONDO_INPUTS))

        self.btn_conectar._canvas.bind("<space>", lambda e: self.controller.handle_login())
        self.btn_conectar._canvas.bind("<Return>", lambda e: self.controller.handle_login())
        self.btn_conectar._canvas.bind("<KP_Enter>", lambda e: self.controller.handle_login())

        self.btn_salir = ctk.CTkButton(self.frame, text="SALIR",
                                       fg_color="#E67E22", hover_color=COLOR_BOTONES_HOVER,
                                       height=45, font=("Arial", 12, "bold"), command=self.quit)
        self.btn_salir.pack(padx=30, pady=10, fill="x")
        self.btn_salir._canvas.configure(takefocus=True, highlightthickness=1, highlightbackground=COLOR_BOTONES_NARANJA_FOCUS)
        self.btn_salir._canvas.bind("<FocusIn>", lambda e: self.btn_salir._canvas.configure(highlightcolor=COLOR_BLANCO))
        self.btn_salir._canvas.bind("<FocusOut>", lambda e: self.btn_salir._canvas.configure(highlightcolor=COLOR_NARANJA))

        # Vincular teclas para Salir
        self.btn_salir._canvas.bind("<space>", lambda e: self.quit())
        self.btn_salir._canvas.bind("<Return>", lambda e: self.quit())
        self.btn_salir._canvas.bind("<KP_Enter>", lambda e: self.quit())


    def get_credentials(self):
        return {
            "empresa": self.combo_empresa.get(),
            "usuario": self.ent_user.get(),
            "pass": self.ent_pass.get()
        }