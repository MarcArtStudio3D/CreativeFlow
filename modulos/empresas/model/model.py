class EmpresaModel:
    def __init__(self, sqlite_model):
        """
        Modelo para gestionar datos de empresas desde SQLite.

        Args:
            sqlite_model: Instancia de DataModel (login/model.py) para acceder a SQLite
        """
        self.sqlite_model = sqlite_model

    def get_datos_empresa(self, id_empresa):
        """Obtiene los datos de una empresa desde SQLite"""
        if self.sqlite_model is None:
            return None, []

        # Usamos el método get_empresa del DataModel
        resultado = self.sqlite_model.get_empresa(id_empresa)
        if not resultado:
            return None, []

        # Para obtener los nombres de columnas de SQLite
        import sqlite3
        try:
            conn = sqlite3.connect(self.sqlite_model.sqlite_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM empresas WHERE id = ? LIMIT 1", (id_empresa,))
            columnas = [description[0] for description in cursor.description]
            conn.close()
        except Exception as e:
            print(f"Error obteniendo nombres de columnas: {e}")
            columnas = []

        return resultado, columnas
