#!/usr/bin/env python3
"""
Convertidor Universal de SQL: SQLite → MariaDB + PostgreSQL
Convierte init_empresa.sql a ambos formatos simultáneamente
"""

import os
import sys

# Importar los convertidores individuales
sys.path.append(os.path.dirname(__file__))

from convert_sql_to_mariadb import convert_sqlite_to_mariadb
from convert_sql_to_postgresql import convert_sqlite_to_postgresql

def main():
    print("=" * 60)
    print("Convertidor Universal de SQL")
    print("SQLite → MariaDB + PostgreSQL")
    print("=" * 60)
    print()

    input_file = 'database/init_empresa.sql'
    output_mariadb = 'database/init_empresa_mariadb.sql'
    output_postgresql = 'database/init_empresa_postgresql.sql'

    try:
        # Convertir a MariaDB
        print("🔄 Convirtiendo a MariaDB...")
        convert_sqlite_to_mariadb(input_file, output_mariadb)
        print("✅ MariaDB: Listo")
        print()

        # Convertir a PostgreSQL
        print("🔄 Convirtiendo a PostgreSQL...")
        convert_sqlite_to_postgresql(input_file, output_postgresql)
        print("✅ PostgreSQL: Listo")
        print()

        print("=" * 60)
        print("✅ CONVERSIÓN COMPLETADA")
        print("=" * 60)
        print()
        print("Archivos generados:")
        print(f"  📄 {output_mariadb}")
        print(f"  📄 {output_postgresql}")
        print()
        print("Resumen de conversiones:")
        print()
        print("MariaDB:")
        print("  • INTEGER → INT")
        print("  • AUTOINCREMENT → AUTO_INCREMENT")
        print("  • Añadido ENGINE=InnoDB")
        print("  • Charset: utf8mb4")
        print()
        print("PostgreSQL:")
        print("  • INTEGER AUTOINCREMENT → SERIAL")
        print("  • TINYINT → SMALLINT")
        print("  • DECIMAL → NUMERIC")
        print("  • updated_at: necesita triggers")

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

