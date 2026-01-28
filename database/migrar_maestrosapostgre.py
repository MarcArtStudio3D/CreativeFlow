import os


def migrar_desde_sqlite(self, db_maestros_pg):
    """
    Lee el SQLite local y lo vuelca en la conexión de Postgres de Maestros.
    """
    import sqlite3
    
    # 1. Ruta al SQLite (ajusta a tu ruta real en Arch)
    path_sqlite = os.path.join(os.path.dirname(__file__), "..", "database", "maestros_local.db")
    
    if not os.path.exists(path_sqlite):
        print("⚠️ No se encontró el SQLite local para migrar.")
        return

    try:
        conn_sqlite = sqlite3.connect(path_sqlite)
        cur_sq = conn_sqlite.cursor()

        # Migrar Países
        cur_sq.execute("SELECT id, nombre, iso FROM paises")
        paises = cur_sq.fetchall()
        for p in paises:
            db_maestros_pg.ejecutar("INSERT INTO paises (id, nombre, iso) VALUES (?, ?, ?) ON CONFLICT DO NOTHING", p)

        # Migrar Monedas
        cur_sq.execute("SELECT id, moneda, nombre_corto, simbolo, cambio FROM monedas")
        for m in cur_sq.fetchall():
            db_maestros_pg.ejecutar("INSERT INTO monedas (id, moneda, nombre_corto, simbolo, cambio) VALUES (?, ?, ?, ?, ?) ON CONFLICT DO NOTHING", m)

        # Migrar Poblaciones (en bloques de 2000 para Arch)
        cur_sq.execute("SELECT id, id_pais, cp, poblacion, poblacion_mayus, region_code, provincia_region FROM poblaciones")
        while True:
            filas = cur_sq.fetchmany(2000)
            if not filas: break
            for f in filas:
                db_maestros_pg.ejecutar("""
                    INSERT INTO poblaciones (id, id_pais, cp, poblacion, poblacion_mayus, region_code, provincia_region) 
                    VALUES (?, ?, ?, ?, ?, ?, ?) ON CONFLICT DO NOTHING
                """, f)
        
        # Ejecutar el reajuste de secuencias final
        db_maestros_pg.ejecutar("SELECT setval(pg_get_serial_sequence('paises', 'id'), coalesce(max(id), 1)) FROM paises")
        db_maestros_pg.ejecutar("SELECT setval(pg_get_serial_sequence('poblaciones', 'id'), coalesce(max(id), 1)) FROM poblaciones")
        
        conn_sqlite.close()
        return True
    except Exception as e:
        print(f"❌ Error en migración: {e}")
        return False