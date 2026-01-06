# componentes.py
import customtkinter as ctk
from colores import *


class AlertaPersonalizada(ctk.CTkToplevel):
    def __init__(self, mensaje, titulo="Error de Acceso"):
        super().__init__()
        self.title(titulo)
        self.geometry("400x200")
        self.configure(fg_color=COLOR_FONDO_PRINCIPAL)
        self.attributes("-topmost", True)  # Que aparezca siempre encima

        # Centrar la ventana
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.winfo_screenheight() // 2) - (200 // 2)
        self.geometry(f"+{x}+{y}")

        # Contenedor
        self.frame = ctk.CTkFrame(self, fg_color=COLOR_FONDO_CONTENEDORES, corner_radius=10)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Icono o Texto de Error
        self.lbl_error = ctk.CTkLabel(
            self.frame,
            text="⚠",
            font=("Arial", 40),
            text_color="#E74C3C"  # Rojo suave
        )
        self.lbl_error.pack(pady=(10, 0))

        self.lbl_mensaje = ctk.CTkLabel(
            self.frame,
            text=mensaje,
            font=("Arial", 12),
            text_color=COLOR_BLANCO,
            wraplength=300  # Para que el texto no se corte
        )
        self.lbl_mensaje.pack(pady=10)

        self.btn_ok = ctk.CTkButton(
            self.frame,
            text="ENTENDIDO",
            width=100,
            fg_color=COLOR_BOTONES,
            hover_color=COLOR_BOTONES_HOVER,
            command=self.destroy
        )
        self.btn_ok.pack(pady=10)