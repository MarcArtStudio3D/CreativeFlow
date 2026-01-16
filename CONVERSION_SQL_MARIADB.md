# Conversión de SQL: SQLite → MariaDB

## 🔴 Problema Original

Al intentar crear la base de datos MariaDB con el script `init_empresa.sql` (diseñado para SQLite), aparecía el error:

```
Error: You have an error in your SQL syntax; check the manual that corresponds to 
your MariaDB server version for the right syntax to use near 'username VARCHAR(50) 
NOT NULL...' at line 2
```

## 🔍 Causa

El archivo `init_empresa.sql` usa **sintaxis específica de SQLite** que **NO es compatible** con MariaDB:

| SQLite | MariaDB | Problema |
|--------|---------|----------|
| `INTEGER` | `INT` | Tipo de dato diferente |
| `AUTOINCREMENT` | `AUTO_INCREMENT` | Diferente palabra clave |
| `INTEGER PRIMARY KEY AUTOINCREMENT` | `INT AUTO_INCREMENT PRIMARY KEY` | Orden diferente |
| `SMALLINT DEFAULT` | `TINYINT(1) DEFAULT` | Booleanos diferentes |
| `);` | `) ENGINE=InnoDB...;` | Falta especificar motor |
| `updated_at TIMESTAMP...` | `...ON UPDATE CURRENT_TIMESTAMP` | Falta ON UPDATE |

## ✅ Solución Implementada

### 1. **Script de Conversión Automática**

Archivo: `/scripts/convert_sql_to_mariadb.py` (Python)

O comando rápido con `sed`:

```bash
cd /home/marc/Artstudio3D/CreativeFlow

cat database/init_empresa.sql | \
  sed 's/INTEGER PRIMARY KEY AUTOINCREMENT/INT AUTO_INCREMENT PRIMARY KEY/g' | \
  sed 's/AUTOINCREMENT/AUTO_INCREMENT/g' | \
  sed 's/\bINTEGER\b/INT/g' | \
  sed 's/SMALLINT DEFAULT/TINYINT(1) DEFAULT/g' | \
  sed 's/TINYINT DEFAULT/TINYINT(1) DEFAULT/g' | \
  sed 's/updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP/updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP/g' | \
  sed 's/^);$/) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;/g' \
  > database/init_empresa_mariadb.sql
```

### 2. **Archivo Generado**

- **Entrada:** `database/init_empresa.sql` (SQLite - 64 tablas)
- **Salida:** `database/init_empresa_mariadb.sql` (MariaDB - 64 tablas)

### 3. **Controller Actualizado**

El controller ahora usa el script correcto:

```python
# ANTES
ruta_sql = os.path.join(project_root, "database", "init_empresa.sql")  # ❌ SQLite

# AHORA
ruta_sql = os.path.join(project_root, "database", "init_empresa_mariadb.sql")  # ✅ MariaDB
```

## 📊 Cambios Realizados

### Ejemplo de tabla convertida:

**ANTES (SQLite):**
```sql
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL,
    activo SMALLINT DEFAULT 1,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**DESPUÉS (MariaDB):**
```sql
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    activo TINYINT(1) DEFAULT 1,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

## ✅ Resultado

- ✅ **64 tablas convertidas** automáticamente
- ✅ **Sintaxis compatible** con MariaDB/MySQL
- ✅ **ENGINE InnoDB** para integridad referencial
- ✅ **UTF8MB4** para soporte completo de Unicode
- ✅ **ON UPDATE CURRENT_TIMESTAMP** para campos updated_at

## 🎯 Uso

```bash
# Opción 1: Script Python
python scripts/convert_sql_to_mariadb.py

# Opción 2: Comando sed (más rápido)
# Ver comando completo arriba
```

## 📝 Notas Importantes

1. **No edites init_empresa_mariadb.sql manualmente**
   - Es un archivo generado automáticamente
   - Edita `init_empresa.sql` y vuelve a convertir

2. **SQLite vs MariaDB**
   - `init_empresa.sql` → Para creativeflow.db (SQLite)
   - `init_empresa_mariadb.sql` → Para empresas en MariaDB

3. **El controller detecta automáticamente**
   - SQLite usa `init_empresa.sql`
   - MariaDB usa `init_empresa_mariadb.sql`

---

**Fecha:** 2026-01-16  
**Estado:** ✅ RESUELTO  
**Tablas convertidas:** 64  
**Compatibilidad:** MariaDB 10.x+ | MySQL 8.0+

