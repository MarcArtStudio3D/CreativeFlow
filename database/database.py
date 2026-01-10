import mysql.connector
import sqlite3
import os

class DataManager:
    def __init__(self, db_config=None):
        """
        Inicializa el DataManager con la configuración de la base de datos.

        Args:
            db_config: Diccionario con la configuración de conexión a MariaDB/MySQL
                      Debe contener: host, port, user, password, database
                      Si es None, se usará una configuración por defecto (para testing)
        """
        if db_config is None:
            # Configuración por defecto solo para casos de emergencia
            self.config = {
                'host': 'localhost',
                'port': 3306,
                'user': 'root',
                'password': '',
                'database': 'creativeflow',
                'charset': 'utf8mb4'
            }
        else:
            self.config = db_config

    def _conectar(self):
        return mysql.connector.connect(**self.config)

    def ejecutar(self, sql, params=None):
        """Para INSERT, UPDATE, DELETE"""
        try:
            conn = self._conectar()
            cursor = conn.cursor()
            cursor.execute(sql, params or ())
            conn.commit()
            cursor.close()
            conn.close()
            return True, "Operación realizada"
        except Exception as e:
            return False, str(e)

    def consultar(self, sql, params=None):
        """Para SELECT (devuelve lista de diccionarios, muy práctico)"""
        try:
            conn = self._conectar()
            # dictionary=True hace que los resultados sean fáciles de leer
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql, params or ())
            res = cursor.fetchall()
            cursor.close()
            conn.close()
            return res
        except Exception as e:
            print(f"Error en consulta: {e}")
            return []

    def fetch_all(self, query, params=None):
        """Este es el método que pedía el módulo Empresas"""
        try:
            conn = self._conectar()
            cursor = conn.cursor()

            # Si es MariaDB y quieres diccionarios, puedes intentar:
            # cursor = conn.cursor(dictionary=True)

            cursor.execute(query, params or ())
            res = cursor.fetchall()

            cursor.close()
            conn.close()
            return res
        except Exception as e:
            print(f"Error en fetch_all: {e}")
            return []

    def get_column_names(self, table_name):
        """Obtiene los nombres de las columnas de una tabla"""
        try:
            conn = self._conectar()
            cursor = conn.cursor()

            # Consulta para obtener información de las columnas
            cursor.execute(f"DESCRIBE {table_name}")
            columns = [column[0] for column in cursor.fetchall()]

            cursor.close()
            conn.close()
            return columns
        except Exception as e:
            print(f"Error obteniendo nombres de columnas: {e}")
            return []

def inicializar_db_desde_archivo(ruta_db, ruta_sql_init, nombre_db, motor, db_config=None):
    """
    Lee un archivo .sql y ejecuta todas sus sentencias en una nueva base de datos.

    Args:
        ruta_db: Ruta al archivo de base de datos (para SQLite)
        ruta_sql_init: Ruta al archivo SQL de inicialización
        nombre_db: Nombre de la base de datos
        motor: 'sqlite' o 'mariaDB'
        db_config: Configuración de conexión (solo para mariaDB). Si es None, se usa config por defecto.
    """
    if motor == 'sqlite':
        # 1. Asegurar que el directorio existe
        os.makedirs(os.path.dirname(ruta_db), exist_ok=True)

        try:
            # 2. Leer el contenido del archivo SQL
            with open(ruta_sql_init, 'r', encoding='utf-8') as f:
                script_sql = f.read()

            # 3. Conectar y ejecutar
            conn = sqlite3.connect(ruta_db)
            cursor = conn.cursor()

            # Usamos executescript para lanzar cientos de líneas de una vez
            cursor.executescript(script_sql)

            conn.commit()
            conn.close()
            print(f"✅ Base de datos '{ruta_db}' creada con éxito desde script.")

        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo SQL en {ruta_sql_init}")
        except sqlite3.Error as e:
            print(f"❌ Error de SQLite al ejecutar el script: {e}")
    elif motor == 'mariaDB':
        try:
            # 1. Preparar configuración sin base de datos específica
            if db_config is None:
                # Configuración por defecto para compatibilidad con código antiguo
                config_sin_db = {
                    'host': 'localhost',
                    'port': 3306,
                    'user': 'root',
                    'password': '',
                    'charset': 'utf8mb4'
                }
            else:
                config_sin_db = db_config.copy()
                config_sin_db.pop('database', None)  # Elimina la clave 'database' si existe

            conn = mysql.connector.connect(**config_sin_db)
            cursor = conn.cursor()

            # 2. Crear la base de datos
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre_db} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
            cursor.execute(f"USE {nombre_db};")

            # 3. Leer el contenido del archivo SQL
            with open(ruta_sql_init, 'r', encoding='utf-8') as f:
                script_sql = f.read()

            # 4. Ejecutar el script SQL
            for statement in script_sql.split(';'):
                stmt = statement.strip()
                if stmt:
                    cursor.execute(stmt)

            conn.commit()
            cursor.close()
            conn.close()
            print(f"✅ Base de datos '{nombre_db}' creada con éxito desde script.")

        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo SQL en {ruta_sql_init}")
        except mysql.connector.Error as e:
            print(f"❌ Error de MariaDB al ejecutar el script: {e}")