import os
import bcrypt
from PySide6.QtSql import QSqlDatabase, QSqlQuery


class DataModel:
    def __init__(self):
        # 1. Obtenemos la ruta absoluta de donde está este archivo (model.py)
        dir_actual = os.path.dirname(os.path.abspath(__file__))

        # 2. Subimos un nivel para llegar a la raíz del proyecto (CreativeFlow/)
        dir_raiz = os.path.dirname(dir_actual)

        # 3. Construimos la ruta completa al archivo .db
        self.sqlite_path = os.path.join(dir_raiz, "creativeflow.db")

        print(f"DEBUG: Buscando base de datos en: {self.sqlite_path}")

        # Inicializar conexión QSqlDatabase
        self._init_db_connection()

    def _init_db_connection(self):
        """Inicializa la conexión a la base de datos SQLite usando QSqlDatabase"""
        connection_name = "creativeflow_main"

        if QSqlDatabase.contains(connection_name):
            self.db = QSqlDatabase.database(connection_name)
        else:
            self.db = QSqlDatabase.addDatabase("QSQLITE", connection_name)
            self.db.setDatabaseName(self.sqlite_path)
            if not self.db.open():
                print(f"Error abriendo la base de datos: {self.db.lastError().text()}")

    def get_empresas_list(self):
        """Devuelve nombres de empresas para el ComboBox"""
        try:
            query = QSqlQuery(self.db)
            if query.exec("SELECT nombre_comercial FROM empresas"):
                res = []
                while query.next():
                    res.append(query.value(0))
                return res
            else:
                print(f"Error en query: {query.lastError().text()}")
                return []
        except Exception as e:
            print(f"Error crítico: ¿Existe el archivo .db? {e}")
            return []

    def get_empresa_id(self, nombre_empresa):
        """Devuelve el ID de la empresa dado su nombre"""
        try:
            query = QSqlQuery(self.db)
            query.prepare("SELECT id FROM empresas WHERE nombre_comercial = ?")
            query.addBindValue(nombre_empresa)

            if query.exec() and query.next():
                return query.value(0)
            else:
                print(f"Error en query: {query.lastError().text()}")
                return None
        except Exception as e:
            print(f"Error crítico: {e}")
            return None

    def get_empresa(self, id_empresa):
        """Devuelve todos los datos de la empresa dado su id"""
        try:
            query = QSqlQuery(self.db)
            query.prepare("SELECT * FROM empresas WHERE id = ?")
            query.addBindValue(id_empresa)

            if query.exec() and query.next():
                # Recopilar todos los valores de la fila
                record = query.record()
                result = tuple(query.value(i) for i in range(record.count()))
                return result
            else:
                print(f"Error en query: {query.lastError().text()}")
                return None
        except Exception as e:
            print(f"Error crítico: {e}")
            return None

    def get_empresa_db_config(self, id_empresa):
        """
        Obtiene la configuración de la base de datos de una empresa específica.

        Args:
            id_empresa: ID de la empresa

        Returns:
            Diccionario con la configuración de conexión a MariaDB/PostgreSQL o None
        """
        try:
            query = QSqlQuery(self.db)

            # Obtenemos los campos de configuración de la base de datos
            sql = """
                SELECT motordb, mariadb_host, mariadb_port, mariadb_name, 
                       mariadb_user, mariadb_password,
                       postgre_host, postgre_port, postgre_name,
                       postgre_user, postgre_password
                FROM empresas 
                WHERE id = ?
            """
            query.prepare(sql)
            query.addBindValue(id_empresa)

            if not query.exec() or not query.next():
                print(f"No se encontró la empresa con ID {id_empresa}")
                return None

            motor = query.value(0) or "MariaDB"

            if motor.lower() == "mariadb":
                return {
                    'host': query.value(1) or 'localhost',
                    'port': int(query.value(2)) if query.value(2) else 3306,
                    'database': query.value(3) or 'creativeflow',
                    'user': query.value(4) or 'root',
                    'password': query.value(5) or '',
                    'charset': 'utf8mb4'
                }
            elif motor.lower() == "postgresql":
                return {
                    'host': query.value(6) or 'localhost',
                    'port': int(query.value(7)) if query.value(7) else 5432,
                    'database': query.value(8) or 'creativeflow',
                    'user': query.value(9) or 'postgres',
                    'password': query.value(10) or '',
                    'motor': 'postgresql'
                }
            else:
                print(f"Motor de base de datos no soportado: {motor}")
                return None

        except Exception as e:
            print(f"Error obteniendo configuración de BD: {e}")
            return None

    def validar_acceso(self, empresa, usuario, password_ingresada):
        try:
            query = QSqlQuery(self.db)

            sql = """
                SELECT u.contrasena, r.nombre_rol
                FROM usuarios u
                JOIN roles r ON u.id_rol = r.id
                WHERE u.nombre = ?
            """
            query.prepare(sql)
            query.addBindValue(usuario)

            if not query.exec() or not query.next():
                return {"success": False, "error": "Usuario no encontrado."}

            hash_db_str = query.value(0)
            rol_nombre = query.value(1)

            # EL TRUCO ESTÁ AQUÍ:
            # 1. Convertimos la password del usuario a bytes
            password_bytes = password_ingresada.encode('utf-8')

            # 2. Convertimos el hash de la base de datos a bytes
            # Si el hash es None o vacío, bcrypt fallará, así que validamos
            if not hash_db_str:
                return {"success": False, "error": "El usuario no tiene contraseña asignada."}

            hash_db_bytes = hash_db_str.encode('utf-8')

            # 3. Comparación binaria
            if bcrypt.checkpw(password_bytes, hash_db_bytes):
                return {"success": True, "rol": rol_nombre}
            else:
                return {"success": False, "error": "Contraseña incorrecta."}


        except Exception as e:
            # Esto capturará el error de 'PyBytes' si algo falla y te lo mostrará en tu popup
            return {"success": False, "error": f"Error técnico: {str(e)}"}