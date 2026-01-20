from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlQuery


class ClienteModel:
    def __init__(self, db_model):
        """
        Modelo para gestionar datos de cliente desde la base de datos.

        Args:
            db_model: Instancia de DataModel para acceder a la base de datos
        """
        self.db_model = db_model

    def get_lista_clientes(self,orden_columna="nombre_fiscal"):
        """
        Retorna un QSqlQueryModel con  los clientes para el QTableView.
        """
        from PySide6.QtSql import QSqlQueryModel


        """
        Crea y devuelve un QSqlQueryModel listo para la tabla.
        """
        model = QSqlQueryModel()

        # IMPORTANTE: En SQL, el ORDER BY no admite bindValue (:order).
        # Debes insertar el nombre de la columna directamente en el string.
        sql = f"SELECT id, nombre_fiscal, nombre_comercial, email, telefono1, poblacion FROM clientes ORDER BY {orden_columna}  LIMIT 100"

        # Ejecutamos la query directamente en el modelo
        model.setQuery(sql, self.db_model.db)

        # Comprobamos si hubo error
        if model.lastError().isValid():
            print(f"Error en SQL: {model.lastError().text()}")

        # Asignamos cabeceras (esto sí lo hace el modelo)
        titulos = ["ID", "Nombre Fiscal", "Nombre Comercial", "Email", "Teléfono", "Población"]
        for i, titulo in enumerate(titulos):
            model.setHeaderData(i, Qt.Horizontal, titulo)


        # 4. (Opcional) Cambiar los nombres de las cabeceras para que queden bien
        model.setHeaderData(0, Qt.Horizontal, "ID")
        model.setHeaderData(1, Qt.Horizontal, "Nombre Fiscal")
        model.setHeaderData(2, Qt.Horizontal, "Nombre Comercial")
        model.setHeaderData(3, Qt.Horizontal, "Email")
        model.setHeaderData(4, Qt.Horizontal, "Teléfono")
        model.setHeaderData(5, Qt.Horizontal, "Población")

        return model



    def get_datos_cliente(self, id_cliente):
        """Obtiene los datos y nombres de columna de un cliente en una sola consulta."""
        if not self.db_model or not self.db_model.db.isOpen():
            print("Error: La base de datos no está abierta.")
            return None, []

        # 1. Preparamos la query directamente sobre la conexión existente
        query = QSqlQuery(self.db_model.db)
        query.prepare("SELECT * FROM clientes WHERE id = :id")
        query.bindValue(":id", id_cliente)

        # 2. Ejecutamos y extraemos todo
        if query.exec() and query.next():
            record = query.record()

            # Extraemos los nombres de las columnas
            columnas = [record.fieldName(i) for i in range(record.count())]

            # Extraemos los valores del registro
            valores = [query.value(i) for i in range(record.count())]

            return valores, columnas
        else:
            error_msg = query.lastError().text()
            print(f"Error al recuperar cliente ID {id_cliente}: {error_msg}")
            return None, []

    def buscar_cliente_por_nombre_fiscal(self, nombre,direccion=0):
        """Busca un cliente por su nombre"""
        if not self.db_model:
            return None, []

        query = QSqlQuery(self.db_model.db)
        if direccion==0:
            query.prepare("SELECT * FROM clientes WHERE nombre_fiscal = ?")
        elif direccion==1: # siguiente
            query.prepare("SELECT * FROM clientes WHERE nombre_fiscal > ?  ORDER BY nombre_fiscal LIMIT 1")
        elif direccion==2: #
            query.prepare("SELECT * FROM clientes WHERE nombre_fiscal < ?  ORDER BY nombre_fiscal DESC LIMIT 1")

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

    def siguiente_cliente_id(self,id_cliente):
        """Obtiene el siguiente ID disponible para un nuevo cliente."""
        query = QSqlQuery(self.db_model.db)
        idcliente = id_cliente + 1
        query.prepare("SELECT * FROM clientes where id = :id_cliente")
        query.bindValue(":id_cliente", idcliente)

        if query.exec() and query.next():
            return True
        else:
            print(f"Error al obtener la ficha del cliente: {query.lastError().text()}")
            return 1