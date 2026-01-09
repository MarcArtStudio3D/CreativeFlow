# CRUDempresas.py
import sqlite3
import config as cfg
import mysql.connector

def guardar_empresa(datos):
    try:
        conn = sqlite3.connect(cfg.DB_NAME)
        cursor = conn.cursor()
        # SQL directo, sin capas ocultas
        query = """INSERT INTO empresas (nombre_fiscal, cif_nif, cp, poblacion, provincia) 
                   VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(query, datos)
        conn.commit()
        conn.close()
        return True, "Guardado con éxito"
    except Exception as err:
        return False, f"Error SQL: {err}"

def obtener_datos_acceso_sqlite(id_empresa):
    """Lee de la SQLite maestra los datos de la MariaDB de esa empresa"""
    conn = sqlite3.connect("creativeflow_master.db")
    cursor = conn.cursor(dictionary=True) # Usamos diccionario para mayor claridad
    cursor.execute("SELECT host, usuario, password, db_name FROM empresas WHERE id = ?", (id_empresa,))
    datos = cursor.fetchone()
    conn.close()
    return datos

def conectar_empresa(datos_acceso):
    """Crea la conexión a la MariaDB específica de la empresa"""
    return mysql.connector.connect(
        host=datos_acceso['host'],
        user=datos_acceso['usuario'],
        password=datos_acceso['password'],
        database=datos_acceso['db_name']
    )