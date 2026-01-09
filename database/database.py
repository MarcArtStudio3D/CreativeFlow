import mysql.connector
import sqlite3
import os
import config as cfg

class DataManager:
    def __init__(self):
        self.config = cfg.DB_CONFIG

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


def inicializar_db_desde_archivo(ruta_db, ruta_sql_init, nombre_db, motor):
    """
    Lee un archivo .sql y ejecuta todas sus sentencias en una nueva base de datos.
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
            # 1. Conectar al servidor sin especificar base de datos
            config_sin_db = cfg.DB_CONFIG.copy()
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