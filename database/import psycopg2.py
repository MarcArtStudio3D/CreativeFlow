import psycopg2
import sqlite3
import os
from decimal import Decimal

def rescatar_maestros_a_sqlite():
    # --- CONFIGURACIÓN ---
    # Datos de la base de datos de la empresa (Postgres)
    pg_config = {
        "host": "localhost",
        "database": "artstudio3d", # <--- Cambia esto
        "user": "postgres",
        "password": "admin123",
        "port": 5432
    }
    
    # Ruta del SQLite local
    sqlite_path = "database/creativeflow.db" 
    
    try:
        # 1. Conectar a Postgres
        pg_conn = psycopg2.connect(**pg_config)
        pg_cur = pg_conn.cursor()
        print("✅ Conectado a PostgreSQL")

        # 2. Conectar a SQLite
        sl_conn = sqlite3.connect(sqlite_path)
        sl_cur = sl_conn.cursor()
        print(f"✅ Conectado a SQLite ({sqlite_path})")

        # --- RESCATAR MONEDAS ---
        print("Migrando monedas...")
        sl_cur.execute("""
            CREATE TABLE IF NOT EXISTS monedas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                moneda TEXT,
                nombre_corto TEXT UNIQUE,
                simbolo TEXT,
                cambio REAL,
                fecha_cambio TEXT,
                created_at TEXT,
                updated_at TEXT
            )
        """)
        
        pg_cur.execute("SELECT moneda, nombre_corto, simbolo, cambio, fecha_cambio, created_at, updated_at FROM monedas")
        for fila in pg_cur.fetchall():
            fila_procesada = [float(x) if isinstance(x, Decimal) else x for x in fila]
            sl_cur.execute("""
                INSERT OR IGNORE INTO monedas 
                (moneda, nombre_corto, simbolo, cambio, fecha_cambio, created_at, updated_at) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, fila_procesada)

        # --- RESCATAR PAÍSES ---
        print("Migrando países...")
        sl_cur.execute("""
            CREATE TABLE IF NOT EXISTS paises (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pais TEXT UNIQUE,
                country_code TEXT UNIQUE,
                id_monedas INTEGER,
                created_at TEXT,
                updated_at TEXT
            )
        """)
        
        pg_cur.execute("SELECT pais, country_code, id_monedas, created_at, updated_at FROM paises")
        for fila in pg_cur.fetchall():
            sl_cur.execute("""
                INSERT OR IGNORE INTO paises 
                (pais, country_code, id_monedas, created_at, updated_at) 
                VALUES (?, ?, ?, ?, ?)
            """, fila)

        sl_conn.commit()
        print("🎉 Datos rescatados con éxito en creativeflow.db")

    except Exception as e:
        print(f"❌ Error durante el rescate: {e}")
    finally:
        if 'pg_conn' in locals(): pg_conn.close()
        if 'sl_conn' in locals(): sl_conn.close()

if __name__ == "__main__":
    rescatar_maestros_a_sqlite()