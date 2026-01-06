import mysql.connector
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