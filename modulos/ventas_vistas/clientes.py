import customtkinter as ctk


class ClientesView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        ctk.CTkLabel(self, text="GESTIÓN DE CLIENTES", font=("Arial", 20, "bold")).pack(pady=10)

        # Aquí pondremos la tabla de SQLite en el siguiente paso
        self.btn_load = ctk.CTkButton(self, text="Refrescar Datos", command=self.load_db)
        self.btn_load.pack()

    def load_db(self):
        print("Conectando a SQLite para traer clientes...")