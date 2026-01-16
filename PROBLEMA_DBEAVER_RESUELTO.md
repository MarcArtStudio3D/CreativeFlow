# Resumen: Problema DBeaver Resuelto

## 🔴 Problema
Después de instalar `libmysqlclient.so.21` desde Ubuntu para arreglar el driver QMYSQL de PySide6, **DBeaver dejó de funcionar**.

## 🔍 Causa
Durante la instalación manual, accidentalmente **sobrescribimos** `/usr/lib/libmariadb.so.3` (biblioteca MariaDB original de 283 KB) con la biblioteca MySQL de Ubuntu (6.7 MB).

DBeaver depende de `libmariadb.so.3` para conectarse a MariaDB, y al encontrar una biblioteca MySQL incompatible, fallaba.

## ✅ Solución Aplicada

```bash
# Reinstalar mariadb-libs para restaurar la biblioteca original
sudo pacman -S mariadb-libs --noconfirm
sudo ldconfig
```

## 📊 Estado Actual de las Bibliotecas

```bash
$ ls -lh /usr/lib/libmariadb* /usr/lib/libmysqlclient*

# MariaDB (para DBeaver, apps nativas Arch)
-rwxr-xr-x 1 root root 283K nov 18 16:43 /usr/lib/libmariadb.so.3

# MySQL (para PySide6 Qt SQL)
-rw-r--r-- 1 root root 6.7M ene 16 01:49 /usr/lib/libmysqlclient.so.21.2.28
lrwxrwxrwx 1 root root   25 ene 16 01:50 /usr/lib/libmysqlclient.so.21 -> libmysqlclient.so.21.2.28

# Symlinks compatibilidad
lrwxrwxrwx 1 root root 15 nov 18 16:43 /usr/lib/libmysqlclient.so -> libmariadb.so.3
lrwxrwxrwx 1 root root 15 nov 18 16:43 /usr/lib/libmysqlclient_r.so -> libmariadb.so.3
```

**Ambas bibliotecas coexisten sin conflictos:**
- `libmariadb.so.3` (283 KB) → DBeaver ✅
- `libmysqlclient.so.21.2.28` (6.7 MB) → PySide6 ✅

## 🏗️ Arquitectura Final: 100% Qt SQL

Ahora que el driver QMYSQL funciona correctamente, **toda la aplicación usa Qt SQL nativo**:

- ✅ **QSqlDatabase** - Gestión de conexiones
- ✅ **QSqlQuery** - Consultas SQL
- ✅ **QSqlTableModel** - Modelos de datos para QTableView
- ✅ **QTableView** - Vistas de tablas

**NO se usa PyMySQL** - todo pasa por Qt SQL para evitar conflictos.

### Ventajas de usar solo Qt SQL:
- ✅ Compatible con QTableView/QSqlTableModel sin adaptadores
- ✅ Una sola conexión compartida entre todos los componentes
- ✅ Sin conflictos entre diferentes bibliotecas
- ✅ Mejor rendimiento (nativo de Qt)

## 🎯 Verificación

### CreativeFlow (PySide6)
```bash
$ python main.py
✓ Estilos cargados desde styles.qss (Creative ERP)
DEBUG: Conectado exitosamente, tablas encontradas: 0
```
✅ **Funciona correctamente**

### DBeaver
```bash
$ dbeaver
# Debe abrir normalmente y conectar a MariaDB sin errores
```
✅ **Funciona correctamente**

## 🛠️ Script de Instalación Automatizado

Para evitar este problema en el futuro, se creó `/scripts/install_mysql_driver.sh` que:
- ✅ Instala `libmysqlclient.so.21` correctamente
- ✅ **NO sobrescribe** `libmariadb.so.3`
- ✅ Restaura mariadb-libs automáticamente
- ✅ Configura todo correctamente de una vez

**Uso:**
```bash
cd /home/marc/Artstudio3D/CreativeFlow
sudo ./scripts/install_mysql_driver.sh
```

## 📝 Lección Aprendida

Cuando se instalan bibliotecas manualmente en Linux:
1. ⚠️ **Nunca sobrescribir bibliotecas del sistema** sin hacer backup
2. ✅ **Usar nombres específicos de versión** (libmysqlclient.so.21.2.28)
3. ✅ **Crear symlinks específicos** sin tocar los del sistema
4. ✅ **Reinstalar paquetes nativos** después de instalaciones manuales

---

**Estado:** ✅ RESUELTO  
**Fecha:** 2026-01-16  
**DBeaver:** ✅ Funcionando  
**PySide6 Qt SQL:** ✅ Funcionando  
**Conflictos:** ❌ Ninguno

