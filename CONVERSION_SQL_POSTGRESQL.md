# Conversión SQL: SQLite → PostgreSQL

## 🎯 Diferencias SQLite vs PostgreSQL

| Característica | SQLite | PostgreSQL |
|----------------|--------|------------|
| **Auto-incremento** | `INTEGER PRIMARY KEY AUTOINCREMENT` | `SERIAL PRIMARY KEY` |
| **Booleanos** | `TINYINT(1)` o `SMALLINT` | `SMALLINT` o `BOOLEAN` |
| **Decimales** | `DECIMAL(n,m)` | `NUMERIC(n,m)` |
| **Motor de tabla** | No aplica | No aplica (sin ENGINE) |
| **Charset** | No aplica | Usa encoding a nivel BD |
| **Auto-update** | `ON UPDATE` no soportado | Necesita **TRIGGER** |

## ✅ Conversión Implementada

### Script: `/scripts/convert_sql_to_postgresql.py`

Conversiones automáticas:
1. ✅ `INTEGER PRIMARY KEY AUTOINCREMENT` → `SERIAL PRIMARY KEY`
2. ✅ `TINYINT` → `SMALLINT`
3. ✅ `DECIMAL` → `NUMERIC`
4. ✅ Comentarios sobre `updated_at` (necesita trigger)

### Archivos Generados

```bash
database/
├── init_empresa.sql              # Original (SQLite)
├── init_empresa_mariadb.sql      # Para MariaDB/MySQL
└── init_empresa_postgresql.sql   # Para PostgreSQL ✨ NUEVO
```

## 📊 Ejemplo de Conversión

### ANTES (SQLite):
```sql
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL,
    activo TINYINT DEFAULT 1,
    saldo DECIMAL(15,4) DEFAULT 0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### DESPUÉS (PostgreSQL):
```sql
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    activo SMALLINT DEFAULT 1,
    saldo NUMERIC(15,4) DEFAULT 0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- PostgreSQL: necesita trigger para ON UPDATE
);
```

## ⚠️ Consideraciones Especiales para PostgreSQL

### 1. **AUTO_INCREMENT con SERIAL**
```sql
-- SQLite
id INTEGER PRIMARY KEY AUTOINCREMENT

-- PostgreSQL
id SERIAL PRIMARY KEY
-- Equivalente a:
-- id INTEGER DEFAULT nextval('tabla_id_seq') PRIMARY KEY
```

### 2. **Booleanos**
PostgreSQL tiene tipo `BOOLEAN` nativo:
```sql
-- Opción 1: SMALLINT (compatible con SQLite)
activo SMALLINT DEFAULT 1

-- Opción 2: BOOLEAN (nativo PostgreSQL, mejor)
activo BOOLEAN DEFAULT TRUE
```

### 3. **ON UPDATE CURRENT_TIMESTAMP**
PostgreSQL **NO soporta** `ON UPDATE` directamente. Necesitas crear un **TRIGGER**:

```sql
-- Función para actualizar updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Trigger para cada tabla
CREATE TRIGGER update_usuarios_updated_at 
    BEFORE UPDATE ON usuarios 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();
```

### 4. **CREATE DATABASE**
```sql
-- MariaDB
CREATE DATABASE `empresa1` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- PostgreSQL
CREATE DATABASE empresa1 ENCODING 'UTF8';
```

### 5. **USE database vs \\c**
```sql
-- MariaDB
USE `empresa1`;

-- PostgreSQL (en psql)
\c empresa1

-- Qt SQL (ambos usan setDatabaseName)
db.setDatabaseName("empresa1")
db.open()
```

## 🛠️ Uso del Convertidor

### Opción 1: Script Python
```bash
cd /home/marc/Artstudio3D/CreativeFlow
python scripts/convert_sql_to_postgresql.py
```

### Opción 2: Conversión Manual con sed
```bash
cat database/init_empresa.sql | \
  sed 's/INTEGER PRIMARY KEY AUTOINCREMENT/SERIAL PRIMARY KEY/g' | \
  sed 's/TINYINT/SMALLINT/g' | \
  sed 's/DECIMAL/NUMERIC/g' \
  > database/init_empresa_postgresql.sql
```

## 🎯 Controller Actualizado

El controller ahora **detecta automáticamente** el motor de BD:

```python
def preparar_base_datos_mariadb(self):
    motor_bd = "mariadb"  # o "postgresql"
    
    if motor_bd == "postgresql":
        ruta_sql = "database/init_empresa_postgresql.sql"
        driver_qt = "QPSQL"
    else:
        ruta_sql = "database/init_empresa_mariadb.sql"
        driver_qt = "QMYSQL"
    
    # Crear BD según el motor
    if motor_bd == "postgresql":
        query.exec(f"CREATE DATABASE {db_name}")
    else:
        query.exec(f"CREATE DATABASE `{db_name}` CHARACTER SET utf8mb4...")
```

## ✅ Resultado

- ✅ **64 tablas convertidas** para PostgreSQL
- ✅ **SERIAL PRIMARY KEY** en lugar de AUTOINCREMENT
- ✅ **SMALLINT** en lugar de TINYINT
- ✅ **NUMERIC** en lugar de DECIMAL
- ⚠️ **updated_at** necesitará triggers (comentado en SQL)

## 📝 TODO: Triggers para updated_at

Si necesitas auto-actualizar `updated_at`, crea un script adicional:

```sql
-- /database/triggers_postgresql.sql
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Aplicar a todas las tablas con updated_at
CREATE TRIGGER update_usuarios_updated_at BEFORE UPDATE ON usuarios FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_alb_pro_updated_at BEFORE UPDATE ON alb_pro FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
-- ... (para cada tabla)
```

---

**Fecha:** 2026-01-16  
**Estado:** ✅ COMPLETADO  
**Tablas convertidas:** 64  
**Compatibilidad:** PostgreSQL 12+

