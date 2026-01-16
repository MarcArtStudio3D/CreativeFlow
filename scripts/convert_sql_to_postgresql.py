#!/usr/bin/env python3
"""
Convertidor de SQL: SQLite → PostgreSQL
Convierte init_empresa.sql (SQLite) a init_empresa_postgresql.sql (PostgreSQL)
"""

import re
import sys

def convert_sqlite_to_postgresql(input_file, output_file):
    """Convierte un archivo SQL de SQLite a PostgreSQL"""

    with open(input_file, 'r', encoding='utf-8') as f:
        sql = f.read()

    # 1. INTEGER PRIMARY KEY AUTOINCREMENT → SERIAL PRIMARY KEY
    sql = re.sub(
        r'INTEGER\s+PRIMARY\s+KEY\s+AUTOINCREMENT',
        'SERIAL PRIMARY KEY',
        sql,
        flags=re.IGNORECASE
    )

    # 2. AUTOINCREMENT → (eliminar, SERIAL ya lo incluye)
    sql = re.sub(r'AUTOINCREMENT', '', sql, flags=re.IGNORECASE)

    # 3. TINYINT → SMALLINT (PostgreSQL no tiene TINYINT)
    sql = re.sub(r'\bTINYINT\b', 'SMALLINT', sql, flags=re.IGNORECASE)

    # 4. DECIMAL → NUMERIC (más estándar en PostgreSQL)
    sql = re.sub(r'\bDECIMAL\b', 'NUMERIC', sql, flags=re.IGNORECASE)

    # 5. DEFAULT NULL → (PostgreSQL prefiere sin DEFAULT para NULL)
    # Pero lo dejamos para compatibilidad

    # 6. Añadir ON UPDATE para updated_at (PostgreSQL necesita trigger, lo comentamos)
    sql = re.sub(
        r'(updated_at\s+TIMESTAMP\s+DEFAULT\s+CURRENT_TIMESTAMP)',
        r'\1 -- PostgreSQL: necesita trigger para ON UPDATE',
        sql,
        flags=re.IGNORECASE
    )

    # 7. Comentar referencias a motores (PostgreSQL no usa ENGINE)
    # No hay ENGINE en el SQL original, así que esto no aplica

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(sql)

    print(f"✓ Convertido: {input_file} → {output_file}")

if __name__ == '__main__':
    input_file = 'database/init_empresa.sql'
    output_file = 'database/init_empresa_postgresql.sql'

    try:
        convert_sqlite_to_postgresql(input_file, output_file)
        print("✓ Conversión completada exitosamente")
        print("\n📝 Notas:")
        print("  - TINYINT → SMALLINT (PostgreSQL no tiene TINYINT)")
        print("  - DECIMAL → NUMERIC (más estándar en PostgreSQL)")
        print("  - INTEGER PRIMARY KEY AUTOINCREMENT → SERIAL PRIMARY KEY")
        print("  - updated_at necesitará trigger para auto-update")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

