import customtkinter as ctk
import sqlite3
import os
from colores import *


class ClientesView(ctk.CTkFrame):
    def __init__(self, master, session):
        super().__init__(master, fg_color="transparent")
        self.session = session

        # Título y Botón Nuevo
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", pady=(0, 20))

        ctk.CTkLabel(header, text="Directorio de Clientes", font=("Inter", 24, "bold")).pack(side="left")
        ctk.CTkButton(header, text="+ Nuevo Cliente", width=140, fg_color="#1f538d").pack(side="right")

        # Área de tabla
        self.crear_tabla()

    def crear_tabla(self):
        # Contenedor con scroll para que el grid no se rompa
        self.scroll_canvas = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll_canvas.pack(fill="both", expand=True, pady=10)

        # Definimos los anchos de columna para que el Grid sea uniforme
        self.column_widths = {0: 0.1, 1: 0.4, 2: 0.2, 3: 0.3}  # Porcentajes o pesos

        # --- CABECERA (Fila 0) ---
        headers = ["ID", "NOMBRE COMERCIAL", "CIF/VAT", "EMAIL CONTACTO"]
        for i, titulo in enumerate(headers):
            label = ctk.CTkLabel(
                self.scroll_canvas,
                text=titulo,
                font=("Inter", 12, "bold"),
                fg_color="#1A1A1A",  # Un poco más oscuro que el fondo
                height=40
            )
            label.grid(row=0, column=i, sticky="nsew", padx=1, pady=1)

        self.scroll_canvas.grid_columnconfigure(1, weight=3)  # Nombre comercial más ancho
        self.scroll_canvas.grid_columnconfigure(3, weight=2)  # Email un poco más ancho

        self.refrescar_datos()

    def refrescar_datos(self):
        db_path = self.session.get('archivo_sqlite')
        if not db_path or not os.path.exists(db_path): return

        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            # Traemos también el ID para que parezca una base de datos real
            cursor.execute("SELECT id, nombre_comercial, cif_siren, email FROM clientes")

            for r_idx, row in enumerate(cursor.fetchall(), start=1):
                for c_idx, valor in enumerate(row):
                    # Cada celda es un Label (o un Entry si quisieras editar in-place)
                    celda = ctk.CTkLabel(
                        self.scroll_canvas,
                        text=str(valor),
                        fg_color="#333333" if r_idx % 2 == 0 else "#2B2B2B",  # Efecto Cebra
                        height=35,
                        anchor="w" if c_idx != 0 else "center"  # ID centrado, resto izquierda
                    )
                    celda.grid(row=r_idx, column=c_idx, sticky="nsew", padx=1, pady=1)

                    # Bonus: Al hacer clic en la celda, podríamos abrir el cliente
                    celda.bind("<Button-1>", lambda e, id_c=row[0]: self.abrir_ficha_cliente(id_c))

            conn.close()
        except Exception as e:
            print(f"Error en Grid: {e}")

    def abrir_ficha_cliente(self, id_cliente):
        print(f"Abriendo ficha del cliente ID: {id_cliente}")