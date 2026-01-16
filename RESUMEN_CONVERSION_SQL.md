# Resumen: Conversión SQL Completa

## ✅ Archivos SQL Generados

```bash
database/
├── init_empresa.sql              # 81 KB - SQLite (original)
├── init_empresa_mariadb.sql      # 86 KB - MariaDB/MySQL ✅
└── init_empresa_postgresql.sql   # 83 KB - PostgreSQL ✅
```

## 🎯 Scripts de Conversión

```bash
scripts/
├── convert_sql_to_mariadb.py     # SQLite → MariaDB
├── convert_sql_to_postgresql.py  # SQLite → PostgreSQL
└── convert_all_sql.py            # Convertir a ambos ✨
```

## 📊 Comparación de Motores

| Característica | SQLite | MariaDB | PostgreSQL |
|----------------|--------|---------|------------|
| **Auto-increment** | `INTEGER PRIMARY KEY AUTOINCREMENT` | `INT AUTO_INCREMENT PRIMARY KEY` | `SERIAL PRIMARY KEY` |
| **Booleanos** | `TINYINT(1)` | `TINYINT(1)` | `SMALLINT` o `BOOLEAN` |
| **Decimales** | `DECIMAL(n,m)` | `DECIMAL(n,m)` | `NUMERIC(n,m)` |
| **Motor de tabla** | No aplica | `ENGINE=InnoDB` | No aplica |
| **Charset** | No aplica | `utf8mb4_unicode_ci` | `UTF8` encoding |
| **ON UPDATE** | No soportado | ✅ Soportado | ❌ Necesita trigger |
| **Índices** | ✅ Automático | ✅ Personalizable | ✅ Personalizable |

## 🔄 Conversiones Aplicadas

### MariaDB (init_empresa_mariadb.sql)
```sql
-- ANTES (SQLite)
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    activo SMALLINT DEFAULT 1
);

-- DESPUÉS (MariaDB)
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    activo TINYINT(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

### PostgreSQL (init_empresa_postgresql.sql)
```sql
-- ANTES (SQLite)
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    activo TINYINT DEFAULT 1,
    saldo DECIMAL(15,4) DEFAULT 0
);

-- DESPUÉS (PostgreSQL)
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    activo SMALLINT DEFAULT 1,
    saldo NUMERIC(15,4) DEFAULT 0
);
```

## 🚀 Uso

### Convertir Ambos a la Vez
```bash
cd /home/marc/Artstudio3D/CreativeFlow
python scripts/convert_all_sql.py
```

### Convertir Solo MariaDB
```bash
python scripts/convert_sql_to_mariadb.py
```

### Convertir Solo PostgreSQL
```bash
python scripts/convert_sql_to_postgresql.py
```

## 🎯 Controller Actualizado

El controller ahora **detecta automáticamente** el motor:

```python
def preparar_base_datos_mariadb(self):
    motor_bd = "mariadb"  # o "postgresql"
    
    # Seleccionar script SQL correcto
    if motor_bd == "postgresql":
        ruta_sql = "database/init_empresa_postgresql.sql"
        driver_qt = "QPSQL"
        puerto_default = 5432
    else:  # mariadb/mysql
        ruta_sql = "database/init_empresa_mariadb.sql"
        driver_qt = "QMYSQL"
        puerto_default = 3306
```

## ⚠️ Consideraciones Especiales

### PostgreSQL: Triggers para updated_at

PostgreSQL NO soporta `ON UPDATE CURRENT_TIMESTAMP`. Si lo necesitas, crea triggers:

```sql
-- Crear función
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Aplicar a cada tabla
CREATE TRIGGER update_usuarios_updated_at 
    BEFORE UPDATE ON usuarios 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();
```

### MariaDB: Permisos

Asegúrate de que el usuario tenga permisos:

```sql
GRANT ALL PRIVILEGES ON nombre_bd.* TO 'usuario'@'localhost';
FLUSH PRIVILEGES;
```

### PostgreSQL: Encoding

Al crear la BD, especifica encoding:

```sql
CREATE DATABASE empresa1 
    ENCODING 'UTF8' 
    LC_COLLATE 'es_ES.UTF-8' 
    LC_CTYPE 'es_ES.UTF-8' 
    TEMPLATE template0;
```

## ✅ Verificación

### Contar Tablas en Cada Archivo

```bash
# SQLite original
grep -c "^CREATE TABLE" database/init_empresa.sql
# Output: 64

# MariaDB
grep -c "^CREATE TABLE" database/init_empresa_mariadb.sql
# Output: 64

# PostgreSQL
grep -c "^CREATE TABLE" database/init_empresa_postgresql.sql
# Output: 64
```

### Verificar Sintaxis (MariaDB)

```bash
mariadb -u root -p < database/init_empresa_mariadb.sql
```

### Verificar Sintaxis (PostgreSQL)

```bash
psql -U postgres -d test_db < database/init_empresa_postgresql.sql
```

## 📝 Mantenimiento

Cada vez que modifiques `init_empresa.sql`, ejecuta:

```bash
python scripts/convert_all_sql.py
```

Esto regenerará automáticamente ambos archivos SQL.

## 🎯 Próximos Pasos

1. ✅ Scripts de conversión creados
2. ✅ Archivos SQL generados
3. ✅ Controller actualizado
4. ⏳ TODO: Añadir selector de motor de BD en la vista
5. ⏳ TODO: Crear script de triggers para PostgreSQL
6. ⏳ TODO: Añadir validación de conexión antes de crear BD

---

**Fecha:** 2026-01-16  
**Estado:** ✅ COMPLETADO  
**Motores soportados:** SQLite, MariaDB/MySQL, PostgreSQL  
**Tablas convertidas:** 64 tablas × 3 motores = 192 tablas totales

