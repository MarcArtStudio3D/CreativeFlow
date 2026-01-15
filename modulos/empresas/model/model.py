from PySide6.QtSql import QSqlQuery


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

        # Para obtener los nombres de columnas de SQLite usando QSqlQuery
        try:
            query = QSqlQuery(self.sqlite_model.db)
            query.prepare("SELECT * FROM empresas WHERE id = ? LIMIT 1")
            query.addBindValue(id_empresa)

            if query.exec() and query.next():
                record = query.record()
                columnas = [record.fieldName(i) for i in range(record.count())]
            else:
                print(f"Error obteniendo nombres de columnas: {query.lastError().text()}")
                columnas = []
        except Exception as e:
            print(f"Error obteniendo nombres de columnas: {e}")
            columnas = []

        return registro, columnas

    def buscar_empresa_por_nombre(self, nombre):
        """Busca una empresa por su nombre (útil para el Login o validaciones)"""
        if not self.sqlite_model:
            return None, []

        query = QSqlQuery(self.sqlite_model.db)
        query.prepare("SELECT * FROM empresas WHERE nombre_empresa = ?")
        query.addBindValue(nombre)

        if query.exec() and query.next():
            record = query.record()
            fila = tuple(query.value(i) for i in range(record.count()))
            columnas = [record.fieldName(i) for i in range(record.count())]
            return fila, columnas
        else:
            return None, []

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

            # Crear la query
            query = QSqlQuery(self.sqlite_model.db)
            sql = f"UPDATE empresas SET {campos} WHERE id = ?"

            # --- BLOQUE DE DEBUG ---
            print("-" * 50)
            print(f"SQL QUERY: {sql}")
            print(f"VALORES: {valores + [id_empresa]}")
            print(f"Nº CAMPOS: {len(datos.keys())} | Nº VALORES: {len(valores)} + ID")
            # -----------------------

            query.prepare(sql)

            # Agregar valores
            for valor in valores:
                query.addBindValue(valor)
            query.addBindValue(id_empresa)

            if query.exec():
                return True
            else:
                print(f"Error ejecutando UPDATE: {query.lastError().text()}")
                return False

        except Exception as e:
            print(f"Excepción al actualizar empresa: {e}")
            return False


        except Exception as e:
            # ESTO ES LO QUE TE DIRÁ QUÉ CAMPO FALLA
            print("!" * 50)
            print(f"ERROR SQLITE: {e}")
            print("!" * 50)
            return False

