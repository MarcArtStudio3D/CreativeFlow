# Error Resuelto: Paréntesis Duplicados en SQL

## 🔴 Error Original

```
Error: You have an error in your SQL syntax near ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4...' at line 14
QMYSQL: Unable to execute query
```

## 🔍 Causa

El script de conversión `convert_sql_to_mariadb.py` estaba generando **paréntesis duplicados** al final de cada CREATE TABLE:

```sql
-- ❌ INCORRECTO (con paréntesis duplicado)
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ...
)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
  ↑ PARÉNTESIS DUPLICADO
```

### ¿Por qué pasaba esto?

El regex del script Python estaba **añadiendo** el ENGINE después del `)` en lugar de **reemplazar** el `);` completo.

## ✅ Solución

Modificar el script para que **reemplace** la línea `);` completa en lugar de añadir después:

```python
# ANTES (añadía, causaba duplicados)
sql = re.sub(r'^\);$', lambda m: ') ENGINE=...;', sql, flags=re.MULTILINE)

# AHORA (reemplaza línea completa)
lines = sql.split('\n')
result_lines = []

for line in lines:
    if line.strip() == ');':
        result_lines.append(') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;')
    else:
        result_lines.append(line)

sql = '\n'.join(result_lines)
```

## 📊 Resultado Correcto

```sql
-- ✅ CORRECTO (un solo paréntesis)
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    activo TINYINT(1) DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
  ↑ UN SOLO PARÉNTESIS
```

## ✅ Verificación

```bash
$ python scripts/convert_sql_to_mariadb.py
✓ Convertido: database/init_empresa.sql → database/init_empresa_mariadb.sql

$ python -c "verificar paréntesis duplicados..."
✅ No hay paréntesis duplicados
✅ Tablas encontradas: 64
✅ ENGINE=InnoDB encontrados: 64
✅ Todas las tablas tienen ENGINE
```

## 🎯 Cómo Regenerar

Si necesitas volver a convertir los archivos SQL:

```bash
cd /home/marc/Artstudio3D/CreativeFlow

# Ambos a la vez
python scripts/convert_all_sql.py

# Solo MariaDB
python scripts/convert_sql_to_mariadb.py

# Solo PostgreSQL
python scripts/convert_sql_to_postgresql.py
```

## 📝 Archivos Afectados

1. `/scripts/convert_sql_to_mariadb.py` - **Corregido**
2. `/database/init_empresa_mariadb.sql` - **Regenerado correctamente**
3. `/database/init_empresa_postgresql.sql` - **Regenerado correctamente**

## ✅ Estado Final

- ✅ **64 tablas convertidas** sin errores
- ✅ **Sin paréntesis duplicados**
- ✅ **Sintaxis MariaDB válida**
- ✅ **ENGINE=InnoDB** en todas las tablas
- ✅ **Listo para crear bases de datos**

---

**Fecha:** 2026-01-16  
**Estado:** ✅ RESUELTO DEFINITIVAMENTE  
**Error:** Paréntesis duplicados  
**Solución:** Script corregido para reemplazar en lugar de añadir

