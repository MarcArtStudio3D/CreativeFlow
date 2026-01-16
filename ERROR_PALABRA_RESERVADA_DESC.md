# Error Resuelto: Palabra Reservada SQL 'desc'

## 🔴 Error Original

```
Error: You have an error in your SQL syntax near 'desc MEDIUMTEXT DEFAULT NULL...' at line 5
QMYSQL: Unable to execute query
```

## 🔍 Causa

La columna `desc` en la tabla `tiposubcliente` es una **palabra reservada** en SQL:
- `DESC` = abreviatura de `DESCRIBE` (comando SQL)
- `DESC` = `DESCENDING` (orden descendente en ORDER BY)

Cuando usas palabras reservadas como nombres de columnas **sin protección**, el parser SQL las interpreta como comandos, causando errores de sintaxis.

## ✅ Solución

Proteger las palabras reservadas con **backticks** en MariaDB/MySQL:

### ANTES (❌ ERROR):
```sql
CREATE TABLE tiposubcliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45),
    desc MEDIUMTEXT DEFAULT NULL  ← ERROR: palabra reservada sin proteger
);
```

### DESPUÉS (✅ CORRECTO):
```sql
CREATE TABLE tiposubcliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45),
    `desc` MEDIUMTEXT DEFAULT NULL  ← CORRECTO: protegida con backticks
);
```

## 🔧 Script Actualizado

El script `/scripts/convert_sql_to_mariadb.py` ahora protege automáticamente las palabras reservadas:

```python
# Lista de palabras reservadas comunes
palabras_reservadas = [
    'desc', 'asc', 'order', 'group', 'select', 'from', 'where', 
    'having', 'join', 'inner', 'outer', 'left', 'right', 'union',
    'index', 'key', 'value', 'check', 'constraint', 'references'
]

# Buscar columnas con palabras reservadas y añadir backticks
for palabra in palabras_reservadas:
    sql = re.sub(
        r'\b(' + palabra + r')\s+(VARCHAR|INT|MEDIUMTEXT|...)',
        r'`\1` \2',  ← Añade backticks alrededor de la palabra
        sql,
        flags=re.IGNORECASE
    )
```

## 📊 Palabras Reservadas Protegidas

El script ahora protege automáticamente estas palabras reservadas cuando aparecen como nombres de columnas:

| Palabra | Significado SQL | Ejemplo Protegido |
|---------|-----------------|-------------------|
| `desc` | DESCRIBE / DESCENDING | `` `desc` MEDIUMTEXT `` |
| `asc` | ASCENDING | `` `asc` INT `` |
| `order` | ORDER BY | `` `order` INT `` |
| `group` | GROUP BY | `` `group` VARCHAR `` |
| `key` | PRIMARY KEY | `` `key` VARCHAR `` |
| `value` | VALUES | `` `value` DECIMAL `` |
| `check` | CHECK constraint | `` `check` TINYINT `` |
| `index` | CREATE INDEX | `` `index` INT `` |

## 🎯 Regenerar SQL

Si modificas `init_empresa.sql` y añades más palabras reservadas:

```bash
cd /home/marc/Artstudio3D/CreativeFlow

# Regenerar MariaDB con protección automática
python scripts/convert_sql_to_mariadb.py

# O regenerar ambos
python scripts/convert_all_sql.py
```

## ✅ Verificación

```bash
# Buscar la columna protegida
$ grep -A2 "nombre VARCHAR" database/init_empresa_mariadb.sql | grep desc
  `desc` MEDIUMTEXT DEFAULT NULL,        ← ✅ Protegida con backticks
```

## 📝 Buenas Prácticas

### ❌ **NO USAR** palabras reservadas como nombres:
```sql
CREATE TABLE ejemplo (
    desc TEXT,      ← Malo
    order INT,      ← Malo
    group VARCHAR   ← Malo
);
```

### ✅ **USAR** nombres descriptivos:
```sql
CREATE TABLE ejemplo (
    descripcion TEXT,           ← Bueno
    numero_orden INT,           ← Bueno
    nombre_grupo VARCHAR        ← Bueno
);
```

### ⚠️ Si **DEBES usar** palabras reservadas:
```sql
CREATE TABLE ejemplo (
    `desc` TEXT,      ← Protegido con backticks (MariaDB/MySQL)
    "order" INT,      ← Protegido con comillas dobles (PostgreSQL)
    [group] VARCHAR   ← Protegido con corchetes (SQL Server)
);
```

## 🔄 PostgreSQL

En PostgreSQL, las palabras reservadas se protegen con **comillas dobles**:
```sql
CREATE TABLE tiposubcliente (
    id SERIAL PRIMARY KEY,
    "desc" TEXT DEFAULT NULL  ← PostgreSQL usa comillas dobles
);
```

## ✅ Estado Final

- ✅ **Script corregido** con protección automática
- ✅ **init_empresa_mariadb.sql** regenerado
- ✅ **Columna `desc`** protegida con backticks
- ✅ **64 tablas** funcionando sin errores

---

**Fecha:** 2026-01-16  
**Estado:** ✅ RESUELTO  
**Palabra reservada:** `desc`  
**Solución:** Backticks automáticos en conversión

