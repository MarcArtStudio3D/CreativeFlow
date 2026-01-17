from PySide6.QtSql import QSqlQuery


class ClienteModel:
    def __init__(self, db_model):
        """
        Modelo para gestionar datos de cliente desde la base de datos.

        Args:
            db_model: Instancia de DataModel para acceder a la base de datos
        """
        self.db_model = db_model

    def get_datos_cliente(self, id_cliente):
        """Obtiene los datos de un cliente desde la base de datos"""
        if self.db_model is None:
            return None, []

        # Usamos el método get_empresa del DataModel
        registro = self.db_model.get_empresa(id_cliente)
        if not registro:
            return None, []

        # Para obtener los nombres de columnas de la tabla clientes usando QSqlQuery
        try:
            query = QSqlQuery(self.db_model.db)
            query.prepare("SELECT * FROM clientes WHERE id = ? LIMIT 1")
            query.addBindValue(id_cliente)

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

    def buscar_cliente_por_nombre_fiscal(self, nombre):
        """Busca un cliente por su nombre"""
        if not self.db_model:
            return None, []

        query = QSqlQuery(self.db_model.db)
        query.prepare("SELECT * FROM clientes WHERE nombre_fiscal = ?")
        query.addBindValue(nombre)

        if query.exec() and query.next():
            record = query.record()
            fila = tuple(query.value(i) for i in range(record.count()))
            columnas = [record.fieldName(i) for i in range(record.count())]
            return fila, columnas
        else:
            return None, []

    def actualizar_cliente(self, id_cliente, datos):
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
            query = QSqlQuery(self.db_model.db)
            sql = f"UPDATE clientes SET {campos} WHERE id = ?"

            # --- BLOQUE DE DEBUG ---
            print("-" * 50)
            print(f"SQL QUERY: {sql}")
            print(f"VALORES: {valores + [id_cliente]}")
            print(f"Nº CAMPOS: {len(datos.keys())} | Nº VALORES: {len(valores)} + ID")
            # -----------------------

            query.prepare(sql)

            # Agregar valores
            for valor in valores:
                query.addBindValue(valor)
            query.addBindValue(id_cliente)

            if query.exec():
                return True
            else:
                print(f"Error al guardar cliente: {query.lastError().text()}")
                return False

        except Exception as e:
            print(f"Excepción al actualizar cliente: {e}")
            return False


        except Exception as e:
            # ESTO ES LO QUE TE DIRÁ QUÉ CAMPO FALLA
            print("!" * 50)
            print(f"ERROR DATABASE: {e}")
            print("!" * 50)
            return False
