import sqlite3
import os
import bcrypt


class DataModel:
    def __init__(self):
        # 1. Obtenemos la ruta absoluta de donde está este archivo (model.py)
        dir_actual = os.path.dirname(os.path.abspath(__file__))

        # 2. Subimos un nivel para llegar a la raíz del proyecto (CreativeFlow/)
        dir_raiz = os.path.dirname(dir_actual)

        # 3. Construimos la ruta completa al archivo .db
        self.sqlite_path = os.path.join(dir_raiz, "creativeflow.db")

        print(f"DEBUG: Buscando base de datos en: {self.sqlite_path}")

    def get_empresas_list(self):
        """Devuelve nombres de empresas para el ComboBox"""
        # Usamos 'uri=True' para que si no existe, falle en lugar de crear una vacía
        try:
            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()
            cursor.execute("SELECT nombre_comercial FROM empresas")
            res = [row[0] for row in cursor.fetchall()]
            conn.close()
            return res
        except sqlite3.OperationalError as e:
            print(f"Error crítico: ¿Existe el archivo .db? {e}")
            return []

    def get_empresa_id(self, nombre_empresa):
        """Devuelve el ID de la empresa dado su nombre"""
        try:
            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM empresas WHERE nombre_comercial = ?", (nombre_empresa,))
            result = cursor.fetchone()
            conn.close()
            return result[0] if result else None
        except sqlite3.OperationalError as e:
            print(f"Error crítico: ¿Existe el archivo .db? {e}")
            return None

    def get_empresa(self, id_empresa):
        """Devuelve todos los datos de la empresa dado su id"""
        try:
            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM empresas WHERE id = ?", (id_empresa,))
            result = cursor.fetchone()
            conn.close()
            return result
        except sqlite3.OperationalError as e:
            print(f"Error crítico: ¿Existe el archivo .db? {e}")
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
            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()

            # Obtenemos los campos de configuración de la base de datos
            query = """
                SELECT motordb, mariadb_host, mariadb_port, mariadb_name, 
                       mariadb_user, mariadb_password,
                       postgre_host, postgre_port, postgre_name,
                       postgre_user, postgre_password
                FROM empresas 
                WHERE id = ?
            """
            cursor.execute(query, (id_empresa,))
            result = cursor.fetchone()
            conn.close()

            if not result:
                print(f"No se encontró la empresa con ID {id_empresa}")
                return None

            motor = result[0] or "MariaDB"

            if motor.lower() == "mariadb":
                return {
                    'host': result[1] or 'localhost',
                    'port': int(result[2]) if result[2] else 3306,
                    'database': result[3] or 'creativeflow',
                    'user': result[4] or 'root',
                    'password': result[5] or '',
                    'charset': 'utf8mb4'
                }
            elif motor.lower() == "postgresql":
                return {
                    'host': result[6] or 'localhost',
                    'port': int(result[7]) if result[7] else 5432,
                    'database': result[8] or 'creativeflow',
                    'user': result[9] or 'postgres',
                    'password': result[10] or '',
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
            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()

            query = """
                    SELECT u.contrasena, r.nombre_rol
                    FROM usuarios u
                             JOIN roles r ON u.id_rol = r.id
                    WHERE u.nombre = ? \
                    """
            cursor.execute(query, (usuario,))
            result = cursor.fetchone()
            conn.close()

            if result:
                hash_db_str = result[0]
                rol_nombre = result[1]

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

            return {"success": False, "error": "Usuario no encontrado."}

        except Exception as e:
            # Esto capturará el error de 'PyBytes' si algo falla y te lo mostrará en tu popup
            return {"success": False, "error": f"Error técnico: {str(e)}"}