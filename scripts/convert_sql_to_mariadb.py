#!/usr/bin/env python3
"""
Convertidor de SQL: SQLite → MariaDB
Convierte init_empresa.sql (SQLite) a init_empresa_mariadb.sql (MariaDB)
"""

import re
import sys

def convert_sqlite_to_mariadb(input_file, output_file):
    """Convierte un archivo SQL de SQLite a MariaDB"""

    with open(input_file, 'r', encoding='utf-8') as f:
        sql = f.read()

    # 1. INTEGER PRIMARY KEY AUTOINCREMENT → INT AUTO_INCREMENT PRIMARY KEY
    sql = re.sub(
        r'INTEGER\s+PRIMARY\s+KEY\s+AUTOINCREMENT',
        'INT AUTO_INCREMENT PRIMARY KEY',
        sql,
        flags=re.IGNORECASE
    )

    # 2. AUTOINCREMENT → AUTO_INCREMENT
    sql = re.sub(r'AUTOINCREMENT', 'AUTO_INCREMENT', sql, flags=re.IGNORECASE)

    # 3. INTEGER → INT
    sql = re.sub(r'\bINTEGER\b', 'INT', sql)

    # 4. SMALLINT DEFAULT → TINYINT(1) DEFAULT (para booleanos)
    sql = re.sub(r'\bSMALLINT\s+DEFAULT', 'TINYINT(1) DEFAULT', sql)

    # 5. TINYINT DEFAULT → TINYINT(1) DEFAULT
    sql = re.sub(r'\bTINYINT\s+DEFAULT', 'TINYINT(1) DEFAULT', sql)

    # 6. ON UPDATE CURRENT_TIMESTAMP para updated_at
    sql = re.sub(
        r'(updated_at\s+TIMESTAMP\s+DEFAULT\s+CURRENT_TIMESTAMP)([,\n])',
        r'\1 ON UPDATE CURRENT_TIMESTAMP\2',
        sql,
        flags=re.IGNORECASE
    )

    # 7. Proteger palabras reservadas SQL con backticks
    palabras_reservadas = [
        'desc', 'asc', 'order', 'group', 'select', 'from', 'where',
        'having', 'join', 'inner', 'outer', 'left', 'right', 'union',
        'index', 'key', 'value', 'check', 'constraint', 'references'
    ]

    # Buscar columnas con palabras reservadas y añadir backticks
    for palabra in palabras_reservadas:
        # Patrón: palabra seguida de espacio y tipo de dato
        # Ejemplo: "desc MEDIUMTEXT" → "`desc` MEDIUMTEXT"
        sql = re.sub(
            r'\b(' + palabra + r')\s+(VARCHAR|INT|INTEGER|TEXT|MEDIUMTEXT|LONGTEXT|DECIMAL|NUMERIC|DATETIME|TIMESTAMP|DATE|TIME|BOOLEAN|TINYINT|SMALLINT|BIGINT)',
            r'`\1` \2',
            sql,
            flags=re.IGNORECASE
        )

    # 8. Añadir ENGINE al final de cada CREATE TABLE
    # Reemplazar "); que termina una tabla por ") ENGINE=..."
    # Buscar líneas que contienen solo ");
    lines = sql.split('\n')
    result_lines = []

    for line in lines:
        # Si la línea es exactamente ");", reemplazar
        if line.strip() == ');':
            result_lines.append(') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;')
        else:
            result_lines.append(line)

    sql = '\n'.join(result_lines)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(sql)

    print(f"✓ Convertido: {input_file} → {output_file}")

if __name__ == '__main__':
    input_file = 'database/init_empresa.sql'
    output_file = 'database/init_empresa_mariadb.sql'

    try:
        convert_sqlite_to_mariadb(input_file, output_file)
        print("✓ Conversión completada exitosamente")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

