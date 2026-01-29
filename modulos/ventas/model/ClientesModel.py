import re
from ast import Return

from PySide6.QtCore import QDate, QDateTime, Qt
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QMessageBox

from modulos.comun.view.DBConsultaView import DBConsultaView


class ClienteModel:
    def __init__(self, db_maestros, db_empresa):
        """
        Modelo para gestionar datos de cliente desde la base de datos.

        Args:
            db_maestros: Instancia de DataManager para acceder a la base de datos maestros (paises, poblaciones)
            db_empresa: Instancia de DataManager para acceder a la base de datos de la empresa
        """
        self.db_empresa = db_empresa
        self.db_maestros = db_maestros
    """-----------------------------------------------------
    Obtiene la lista de clientes para el QTableView.
    -----------------------------------------------------"""
    def get_lista_clientes(self,orden_columna="nombre_fiscal", filtro=""):
        """
        Retorna un QSqlQueryModel con  los clientes para el QTableView.
        """
        mapa_columnas = {
            # Español
            "Nombre Fiscal": "nombre_fiscal",
            "Nombre Comercial": "nombre_comercial",
            "NIF": "nif",
            "Población": "poblacion",
            "Email": "email",
            "Teléfono": "telefono1",

            # Francés (si tu app lo requiere)
            "Nom Fiscal": "nombre_fiscal",
            "Nom Commercial": "nombre_comercial",
            "Ville": "poblacion",
            "E-mail": "email",
            "Téléphone": "telefono1"
        }

        # El 'OTHERWISE' de FoxPro es el segundo argumento de .get()
        columna_db = mapa_columnas.get(orden_columna, "nombre_fiscal")
        from PySide6.QtSql import QSqlQueryModel


        """
        Crea y devuelve un QSqlQueryModel listo para la tabla.
        """
        model = QSqlQueryModel()

        # IMPORTANTE: En SQL, el ORDER BY no admite bindValue (:order).
        # Debes insertar el nombre de la columna directamente en el string.
        sql = f"SELECT id, nombre_fiscal, nombre_comercial, email, telefono1, poblacion FROM clientes where unaccent({columna_db}) ilike unaccent('%{filtro}%')  ORDER BY {columna_db}  LIMIT 100"

        # Ejecutamos la query directamente en el modelo
        model.setQuery(sql, self.db_empresa.db)

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

    """-----------------------------------------------------
    Obtiene los datos de un cliente y los nombres de columna.
    -----------------------------------------------------"""
    def get_datos_cliente(self, id_cliente):
        """Obtiene los datos y nombres de columna de un cliente en una sola consulta."""
        if not self.db_empresa or not self.db_empresa.db.isOpen():
            print("Error: La base de datos no está abierta.")
            return None, []

        # 1. Preparamos la query directamente sobre la conexión existente
        query = QSqlQuery(self.db_empresa.db)
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

    """--------------------------------------
    Busca un cliente por su nombre fiscal.
    --------------------------------------"""
    def buscar_cliente_por_nombre_fiscal(self, nombre,direccion=0):
        """Busca un cliente por su nombre"""
        if not self.db_empresa:
            return None, []

        query = QSqlQuery(self.db_empresa.db)

        if direccion==0:
            query.prepare("SELECT * FROM clientes WHERE nombre_fiscal = :nombre")
        elif direccion==1: # siguiente
            query.prepare("SELECT * FROM clientes WHERE nombre_fiscal > :nombre ORDER BY nombre_fiscal LIMIT 1")
        elif direccion==2: # anterior
            query.prepare("SELECT * FROM clientes WHERE nombre_fiscal < :nombre ORDER BY nombre_fiscal DESC LIMIT 1")

        query.bindValue(":nombre", nombre)

        if query.exec() and query.next():
            record = query.record()
            fila = tuple(query.value(i) for i in range(record.count()))
            columnas = [record.fieldName(i) for i in range(record.count())]
            return fila, columnas
        else:
            return None, []

    """---------------------------------------------------------------------
    Actualiza los datos de un cliente en la base de datos de forma dinámica.
    ---------------------------------------------------------------------"""
    def actualizar_cliente(self, id_cliente, datos):
        if not datos:
            return False

        try:
            datos_limpios = {}
            for col, valor in datos.items():
                if col.lower() == 'id':
                    continue

                val_str = str(valor)

                # 1. SI ES UN OBJETO QDATE TEXTUALIZADO (PySide6.QtCore.QDate(2025, 3, 25))
                if "QDate" in val_str:
                    # Buscamos solo los números dentro de los paréntesis
                    # El patrón r'\((\d+),\s*(\d+),\s*(\d+)\)' busca (año, mes, día)
                    match = re.search(r'\((\d+),\s*(\d+),\s*(\d+)\)', val_str)

                    if match:
                        anio, mes, dia = match.groups()
                        if anio != "0":  # Evitar QDate(0, 0, 0)
                            # Formateamos con ceros a la izquierda (YYYY-MM-DD)
                            datos_limpios[col] = f"{anio}-{mes.zfill(2)}-{dia.zfill(2)}"
                        else:
                            datos_limpios[col] = None
                    else:
                        datos_limpios[col] = None

                # 2. MANEJO DE VACÍOS
                elif valor == "" or valor is None or val_str == "None":
                    datos_limpios[col] = None

                # 3. RESTO DE DATOS
                else:
                    datos_limpios[col] = valor

            # --- DEBUG FINAL ---
            print(f"VALORES LIMPIOS: {datos_limpios.get('fecha_alta', 'N/A')}")

            # Construcción de la query con placeholders nombrados
            campos = ", ".join([f"{col} = :{col}" for col in datos_limpios.keys()])

            sql = f"UPDATE clientes SET {campos} WHERE id = :id_cliente"
            query = QSqlQuery(self.db_empresa.db)
            query.prepare(sql)

            # Agregamos los valores con bindValue
            for col, valor in datos_limpios.items():
                query.bindValue(f":{col}", valor)

            # El ID del WHERE
            query.bindValue(":id_cliente", int(id_cliente))

            if query.exec():
                return True
            else:
                print(f"Error SQL: {query.lastError().text()}")
                return False

        except Exception as e:
            # ESTO ES LO QUE TE DIRÁ QUÉ CAMPO FALLA
            print("!" * 50)
            print(f"ERROR DATABASE: {e}")
            print("!" * 50)
            return False

    """-------------------------------------------------------
     Obtiene el siguiente cliente ordenado por ID.
     -------------------------------------------------------"""
    def siguiente_cliente_id(self,id_cliente):
        """Obtiene el siguiente ID disponible para un nuevo cliente."""
        query = QSqlQuery(self.db_empresa.db)
        idcliente = id_cliente + 1
        query.prepare("SELECT * FROM clientes where id = :id_cliente")
        query.bindValue(":id_cliente", idcliente)

        if query.exec() and query.next():
            return True
        else:
            print(f"Error al obtener la ficha del cliente: {query.lastError().text()}")
            return 1

    """---------------------------
    CARGA DE DATOS AUXILIARES
    ---------------------------"""

    def obtener_datos_tabla_auxiliar(self, tabla, campos="*", orden=None, db_key="default"):
        """
        Obtiene datos de una tabla auxiliar.
        Para paises y poblaciones usa db_maestros, para el resto db_empresa.
        """
        # Determinar qué base de datos usar según la tabla
        if tabla.lower() in ["paises", "poblaciones"]:
            connection_name = self.db_maestros.connection_name
        else:
            connection_name = self.db_empresa.connection_name

        # Obtener la conexión por nombre (esto garantiza que siempre es la correcta)
        db_conexion = QSqlDatabase.database(connection_name)

        if not db_conexion or not db_conexion.isOpen():
            print(f"❌ Error: La conexión '{connection_name}' no está abierta para la tabla '{tabla}'.")
            return []

        string_campos = ", ".join(campos) if isinstance(campos, list) else campos
        sql = f"SELECT {string_campos} FROM {tabla}"

        campo_orden = orden if orden else (campos[0] if isinstance(campos, list) and campos[0] != "*" else None)
        if campo_orden and campo_orden != "*":
            sql += f" ORDER BY {campo_orden} ASC"

        # Pasamos la conexión específica a la query usando el nombre de conexión
        query = QSqlQuery(db_conexion)

        if not query.exec(sql):
            print(f"❌ ERROR SQL en [{db_key} - {tabla}]: {query.lastError().text()}")
            return []

        resultados = []
        num_columnas = query.record().count()
        nombres_columnas = [query.record().fieldName(i) for i in range(num_columnas)]

        while query.next():
            if num_columnas == 1:
                resultados.append(query.value(0))
            else:
                # Devolver diccionario para facilitar el acceso por nombre de columna
                fila = {nombres_columnas[i]: query.value(i) for i in range(num_columnas)}
                resultados.append(fila)

        return resultados

    """--------------------------------------
    Buscar Poblaciones por Código Postal
    --------------------------------------"""
    def buscar_poblaciones_por_cp(self, id_pais, cp):
        """
        Busca poblaciones por código postal.

        Args:
            id_pais: ID del país (1=España, 2=Francia, etc.)
            cp: Código postal a buscar

        Returns:
            Lista de diccionarios con los datos de las poblaciones encontradas
        """
        # DEBUG: Mostrar valores de entrada
        print(f"🔍 DEBUG buscar_poblaciones_por_cp:")
        print(f"   - id_pais: {id_pais} (tipo: {type(id_pais)})")
        print(f"   - cp: {cp} (tipo: {type(cp)})")
        print(f"   - Conexión: {self.db_maestros.connection_name}")
        print(f"   - Base de datos: {self.db_maestros.db.databaseName()}")
        print(f"   - Conexión abierta: {self.db_maestros.db.isOpen()}")

        # Ejecutamos directamente sin prepare para evitar problemas con PostgreSQL
        query = QSqlQuery(self.db_maestros.db)

        # Escapamos el CP de forma segura
        cp_safe = str(cp).replace("'", "''")

        sql = f"""SELECT id, poblacion, provincia_region, cp, cp_adicionales
                 FROM poblaciones
                 WHERE id_pais = {int(id_pais)} AND (cp = '{cp_safe}' OR cp_adicionales LIKE '%{cp_safe}%')"""

        print(f"🔍 DEBUG SQL ejecutando:")
        print(f"   {sql}")

        if not query.exec(sql):
            error_msg = query.lastError().text()
            print(f"❌ Error SQL: {error_msg}")
            return []

        poblaciones = []
        while query.next():
            poblaciones.append({
                "id": query.value("id"),
                "poblacion": query.value("poblacion"),
                "provincia_region": query.value("provincia_region"),
                "cp": query.value("cp"),
                "cp_adicionales": query.value("cp_adicionales")
            })

        print(f"🔍 DEBUG: Encontrados {len(poblaciones)} resultados")
        if len(poblaciones) > 0:
            print(f"   Primer resultado: {poblaciones[0]}")

        return poblaciones


    """--------------------------------------
    Buscar Poblaciones por Nombre
    --------------------------------------"""
    def buscar_poblaciones_por_nombre(self, id_pais, nombre):
        """
        Busca poblaciones por nombre de población.

        Args:
            id_pais: ID del país (1=España, 2=Francia, etc.)
            nombre: Nombre de la población a buscar

        Returns:
            Lista de diccionarios con los datos de las poblaciones encontradas
        """
        # Uso el método consultar del DataManager que ya funciona
        sql = """SELECT poblacion, provincia_region, cp, region_code
                 FROM poblaciones
                 WHERE id_pais = ? AND (poblacion LIKE ?)"""
        
        params = [id_pais, f"%{nombre}%"]
        
        try:
            resultados = self.db_maestros.consultar(sql, params)
            return resultados if resultados else []
        except Exception as e:
            print(f"❌ Error SQL buscando poblaciones por nombre: {e}")
            return []

    """--------------------------------------
                Buscar Países
    --------------------------------------"""
    def buscar_paises(self, criterio):
        """
        Abre el selector de países.
        """
        # Usamos db_maestros para paises
        db = self.db_maestros.db

        if not db or not db.isOpen():
            print("La base de datos maestros no está abierta.")
            return

        # Instanciamos el buscador genérico
        buscador = DBConsultaView(db)

        buscador.set_config(
            titulo="Seleccione País",
            sql_base="SELECT id, nombre, iso FROM paises",
            campos_busqueda=["nombre", "iso"],
            headers=["ID", "País", "Código ISO"],
        )
        buscador.set_tamano_columnas([0, 600, 80])

        if buscador.exec():
            # Recuperamos el ID y el nombre
            id_pais = buscador.id_seleccionado
            nombre_pais = buscador.registro.value("nombre")
            DatosPais = {"id": id_pais, "nombre": nombre_pais}
            # Actualizamos la vista de empresas
            return DatosPais
            # Guardamos el ID en alguna parte para el UPDATE
            # (podrías agregar un campo oculto en la vista o un atributo temporal)
