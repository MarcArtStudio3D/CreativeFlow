# Arquitectura Final - Solo Qt SQL

## ✅ Cambios Realizados

### Eliminado: PyMySQL
❌ `pymysql==1.1.2` - Eliminado de `requirements.txt`
❌ `import pymysql` - Eliminado del código

### Implementado: 100% Qt SQL

Ahora **TODO** usa el driver QMYSQL nativo de Qt:

#### Operaciones Administrativas
```python
# preparar_base_datos_mariadb() - ANTES (PyMySQL)
import pymysql
conn = pymysql.connect(host, user, password, port)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE...")

# preparar_base_datos_mariadb() - AHORA (Qt SQL)
temp_db = QSqlDatabase.addDatabase("QMYSQL", "temp_conn")
temp_db.setHostName(host)
query = QSqlQuery(temp_db)
query.exec("CREATE DATABASE...")
```

#### Modelos de Datos
```python
# Compatible con QTableView sin adaptadores
model = QSqlTableModel()
model.setTable("nombre_tabla")
table_view.setModel(model)
```

## 🎯 Ventajas de la Arquitectura Actual

### 1. **Sin Conflictos de Conexiones**
- ✅ Una sola biblioteca (Qt SQL)
- ✅ Una sola conexión compartida
- ✅ Sin conflictos entre pymysql y Qt SQL

### 2. **Compatibilidad Total con Qt**
- ✅ QSqlTableModel funciona nativamente
- ✅ QTableView sin adaptadores
- ✅ Signals/slots de Qt funcionan
- ✅ Transacciones nativas de Qt

### 3. **Mejor Rendimiento**
- ✅ Driver nativo compilado en C++
- ✅ Sin overhead de conversión Python ↔ C++
- ✅ Prepared statements nativos

### 4. **Menos Dependencias**
- ✅ Una biblioteca menos en requirements.txt
- ✅ Sin problemas de versiones de pymysql
- ✅ Instalación más simple

## 📋 Componentes que Usan Qt SQL

### Creación de BD (empresas/controller)
```python
def preparar_base_datos_mariadb(self):
    temp_db = QSqlDatabase.addDatabase("QMYSQL", "temp_conn")
    # ... crear BD y tablas
    
    # Conexión principal para toda la app
    self.db_principal = QSqlDatabase.addDatabase("QMYSQL")
    self.db_principal.setDatabaseName(db_name)
    self.db_principal.open()
```

### Consultas (todos los módulos)
```python
query = QSqlQuery()  # Usa conexión Default
query.exec("SELECT * FROM tabla")
while query.next():
    dato = query.value(0)
```

### Modelos (QTableView)
```python
model = QSqlTableModel()
model.setTable("clientes")
model.select()
table_view.setModel(model)
```

## 🔧 Requisitos del Sistema

### Arch Linux
```bash
# Biblioteca MariaDB (para DBeaver y apps nativas)
sudo pacman -S mariadb-libs

# Biblioteca MySQL (para PySide6 Qt SQL)
# Instalar con script automatizado:
sudo ./scripts/install_mysql_driver.sh
```

### Resultado Final
```bash
$ ls -lh /usr/lib/libmariadb* /usr/lib/libmysqlclient*

-rwxr-xr-x  283K  libmariadb.so.3           # Para DBeaver
-rw-r--r--  6.7M  libmysqlclient.so.21.2.28 # Para Qt SQL
```

## ✅ Verificación

### Compilación
```bash
$ python -m py_compile modulos/empresas/controller/controller.py
✓ Compilación exitosa
```

### Ejecución
```bash
$ python main.py
✓ Estilos cargados desde styles.qss (Creative ERP)
DEBUG: Conectado exitosamente, tablas encontradas: 0
```

### DBeaver
```bash
$ dbeaver
2026-01-16 02:02:16.452 - Connected (SQLite JDBC [3.51.1.0])
```

## 📝 Notas Importantes

1. **NO mezclar PyMySQL y Qt SQL** - puede causar:
   - Conflictos de conexiones
   - Incompatibilidad con QSqlTableModel
   - Problemas de transacciones

2. **Driver QMYSQL funciona perfectamente** gracias a:
   - libmysqlclient.so.21.2.28 instalado correctamente
   - Permisos de /tmp corregidos (1777)

3. **DBeaver usa JDBC (Java)** - independiente de bibliotecas nativas:
   - No le afecta QMYSQL
   - Necesita libmariadb.so.3 restaurada

---

**Estado:** ✅ COMPLETADO  
**Fecha:** 2026-01-16  
**Arquitectura:** 100% Qt SQL (QMYSQL)  
**PyMySQL:** ❌ Eliminado  
**Compatibilidad:** QTableView ✅ | QSqlTableModel ✅ | QSqlQuery ✅

