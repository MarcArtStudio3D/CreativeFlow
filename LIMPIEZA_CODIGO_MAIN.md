# Limpieza de Código Obsoleto - main.py

## 🧹 Código Eliminado

### ❌ Precarga de libmariadb (OBSOLETO)

**Eliminado:**
```python
import ctypes

# ...

try:
    if sys.platform == "linux":
        # Buscamos la librería de forma dinámica en el sistema
        ctypes.CDLL("libmariadb.so.3")
    elif sys.platform == "win32":
        ctypes.CDLL("libmariadb.dll")
    elif sys.platform == "darwin":
        ctypes.CDLL("libmariadb.dylib")
except Exception as e:
    print(f"Aviso: No se pudo precargar la librería nativa: {e}")
```

### ❌ Imports no utilizados

**Eliminado:**
```python
import ctypes
import PySide6
from PySide6.QtCore import Qt, QCoreApplication
```

## 🎯 ¿Por qué era obsoleto?

### 1. **Precarga de libmariadb.so.3**
- ❌ Qt SQL usa **libmysqlclient.so.21** (MySQL), NO libmariadb
- ❌ Precargar libmariadb puede causar conflictos de símbolos
- ❌ El driver QMYSQL ya encuentra libmysqlclient.so.21 automáticamente
- ❌ No aporta ningún beneficio, solo confusión

### 2. **Era un workaround temporal**
Este código fue añadido cuando intentábamos resolver el problema del driver QMYSQL, pensando que ayudaría a que Qt encontrara las bibliotecas. Ahora que:
- ✅ libmysqlclient.so.21 está correctamente instalado
- ✅ El driver QMYSQL funciona perfectamente
- ✅ Ya no necesitamos workarounds

### 3. **Imports innecesarios**
- `ctypes` solo se usaba para precargar la biblioteca (ya eliminado)
- `PySide6` sin usar
- `Qt`, `QCoreApplication` sin usar

## ✅ Código Limpio Final

```python
import os
import sys

from PySide6.QtCore import QTranslator, QLocale
from PySide6.QtWidgets import QApplication
from helpers.messagebox_styles import MessageBoxStyler


def aplicar_estilo_personalizado(app):
    # ...


def main():
    # Suprimir warnings de drivers SQL que no afectan la funcionalidad
    os.environ["QT_LOGGING_RULES"] = "qt.sql.qsqldatabase.warning=false"
    
    app = QApplication(sys.argv)

    # Cargar traductor
    translator = QTranslator()
    idioma = QLocale.system().name()
    if translator.load(f"translations/app_{idioma}.qm"):
        app.installTranslator(translator)

    app.setApplicationName("Creative Flow - Projects Pipeline System")

    # Aplicar el QSS de Creative ERP
    aplicar_estilo_personalizado(app)

    # Instalar el interceptor global de QMessageBox
    messagebox_styler = MessageBoxStyler()
    app.installEventFilter(messagebox_styler)
    print("✓ Estilos automáticos de QMessageBox activados")

    # Iniciar controlador
    from login.controller import LoginController
    login_ctrl = LoginController()

    login_ctrl.view.show()
    sys.exit(app.exec())
```

## 📊 Comparación

| Aspecto | Antes | Después |
|---------|-------|---------|
| Líneas de código | ~70 | ~55 |
| Imports | 7 | 4 |
| Workarounds | 1 (ctypes.CDLL) | 0 |
| Claridad | ❌ Confuso | ✅ Limpio |
| Mantenibilidad | ❌ Baja | ✅ Alta |

## ✅ Verificación

```bash
# Compilación
$ python -m py_compile main.py
✓ Compilación exitosa

# Sin errores de linting
$ get_errors main.py
No errors found.

# Ejecución
$ python main.py
✓ Estilos cargados desde styles.qss (Creative ERP)
✓ Estilos automáticos de QMessageBox activados
DEBUG: Conectado exitosamente
```

## 📝 Notas

- **libmysqlclient.so.21** es encontrado automáticamente por el sistema de carga dinámica de Linux
- **No necesitamos precargar bibliotecas manualmente**
- **El driver QMYSQL funciona out-of-the-box** con la configuración actual

---

**Fecha:** 2026-01-16  
**Estado:** ✅ Código limpio y optimizado  
**Cambios:** Eliminados workarounds obsoletos  
**Resultado:** main.py más limpio y mantenible

