import sqlite3
import os

def fusionar_bases_datos_poblaciones():
    # Rutas relativas según tu estructura
    db_principal = "creativeflow.db"
    db_francia = os.path.join("database", "france.db")
    db_espana = os.path.join("database", "spain.sqlite")

    # Verificación de seguridad
    if not os.path.exists(db_francia) or not os.path.exists(db_espana):
        print("Error: No se encuentran las bases de datos en la carpeta /database")
        return

    # Conectamos a la principal (en la raíz)
    conn = sqlite3.connect(db_principal)
    cursor = conn.cursor()

    try:
        print("Conectando bases de datos externas...")
        # Usamos f-strings para las rutas
        cursor.execute(f"ATTACH DATABASE '{db_francia}' AS db_fra")
        cursor.execute(f"ATTACH DATABASE '{db_espana}' AS db_esp")

        # 1. Crear la tabla unificada
        print("Preparando tabla 'poblaciones'...")
        cursor.execute("DROP TABLE IF EXISTS poblaciones")
        cursor.execute("""
            CREATE TABLE poblaciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_pais INTEGER,
                cp TEXT,
                poblacion TEXT,
                poblacion_mayus TEXT,
                region_code TEXT,
                provincia_region TEXT,
                cp_adicionales TEXT,
                codigo_extra TEXT
            )
        """)

        # 2. Migrar España (id_pais = 57)
        # Usamos los 2 primeros dígitos del CP como region_code (08, 28, etc.)
        print("Migrando datos de España...")
        cursor.execute("""
            INSERT INTO poblaciones (id_pais, cp, poblacion, poblacion_mayus, region_code, provincia_region)
            SELECT 57, cp, poblacion, UPPER(poblacion), SUBSTR(cp, 1, 2), provincia 
            FROM db_esp.cp_info
        """)

        # 3. Migrar Francia (id_pais = 64)
        print("Migrando datos de Francia...")
        cursor.execute("""
            INSERT INTO poblaciones (id_pais, cp, poblacion, poblacion_mayus, region_code, provincia_region, cp_adicionales, codigo_extra)
            SELECT 64, code_postal, nom_standard, nom_standard_majuscule, reg_code, reg_nom, codes_postaux, code_insee 
            FROM db_fra.villes
        """)

        # 4. Crear índices (Indispensable para que sea instantáneo)
        print("Optimizando con índices...")
        cursor.execute("CREATE INDEX idx_pob_pais_cp ON poblaciones(id_pais, cp)")
        cursor.execute("CREATE INDEX idx_pob_pais_nom ON poblaciones(id_pais, poblacion_mayus)")
        cursor.execute("CREATE INDEX idx_pob_region ON poblaciones(id_pais, region_code)")

        conn.commit()
        print("\n¡Éxito! La tabla 'poblaciones' ahora es maestra y única.")
        print(f"Países procesados: España (57) y Francia (64).")

    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
    finally:
        # Limpiar conexiones
        try:
            cursor.execute("DETACH DATABASE db_fra")
            cursor.execute("DETACH DATABASE db_esp")
        except:
            pass
        conn.close()

if __name__ == "__main__":
    fusionar_bases_datos_poblaciones()