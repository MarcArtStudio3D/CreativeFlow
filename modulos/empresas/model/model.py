import sqlite3
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
        registro = self.sqlite_model.get_empresa(id_empresa)
        if not registro:
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

        return registro, columnas

    def buscar_empresa_por_nombre(self, nombre):
        """Busca una empresa por su nombre (útil para el Login o validaciones)"""
        if not self.sqlite_model: return None, []

        query = "SELECT * FROM empresas WHERE nombre_empresa = ?"
        cursor = self.sqlite_model.db.cursor()
        cursor.execute(query, (nombre,))

        fila = cursor.fetchone()
        columnas = [desc[0] for desc in cursor.description] if fila else []

        return fila, columnas

    def actualizar_empresa(self, id_empresa, datos):
        """
        Actualiza los registros de forma dinámica.
        'datos' es el diccionario que viene del controlador.
        """
        if not datos:
            return False

        try:
            # Construimos la parte "CAMPO = ?" del SQL
            campos = ", ".join([f"{col} = ?" for col in datos.keys()])
            valores = list(datos.values())
            valores.append(id_empresa)  # El último '?' es para el WHERE id = ?
            #conectamos y ejecutamos
            try:
                conn = sqlite3.connect(self.sqlite_model.sqlite_path)
                cursor = conn.cursor()
                sql = f"UPDATE empresas SET {campos} WHERE id = ?"
                # --- BLOQUE DE DEBUG ---
                print("-" * 50)
                print(f"SQL QUERY: {sql}")
                print(f"VALORES: {valores}")
                print(f"Nº CAMPOS: {len(datos.keys())} | Nº VALORES: {len(valores) - 1} + ID")
                # -----------------------
                cursor = conn.cursor()
                cursor.execute(sql, valores)
                conn.commit()
                conn.close()

                return True
            except Exception as e:
                print(f"Error obteniendo nombres de columnas: {e}")
                columnas = []


        except Exception as e:
            # ESTO ES LO QUE TE DIRÁ QUÉ CAMPO FALLA
            print("!" * 50)
            print(f"ERROR SQLITE: {e}")
            print("!" * 50)
            return False

