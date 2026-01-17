# 📋 Guía para Importar Pantallas desde Qt Designer

## ✅ **Garantía: Las pantallas heredarán automáticamente el estilo de Creative ERP**

Después de haber copiado el `modern.qss` de Creative ERP, **TODAS las pantallas que compiles desde `.ui` se verán correctamente sin código adicional**.

---

## 🚀 **Proceso Simple (3 pasos)**

### 1️⃣ **Diseñar o editar en Qt Designer**

```bash
# Abrir Qt Designer
qtcreator

# O editar un archivo existente
qtcreator ui/mi_pantalla.ui
```

**Guarda el archivo en la carpeta correcta:**
- Pantallas generales: `ui/` 
- Pantallas de módulos: dentro del módulo correspondiente

---

### 2️⃣ **Compilar el `.ui` a `.py`**

#### **Opción A: Compilar TODO (recomendado)**

```bash
cd /home/marc/Artstudio3D/CreativeFlow
./scripts/compile_ui.sh
```

Este script:
- ✅ Compila todos los `.ui` a `.py`
- ✅ Compila el archivo `.qrc` (recursos/iconos)
- ✅ Elimina código de paleta que bloquea estilos
- ✅ Corrige imports de `designer_rc`
- ✅ Limpia colores hardcodeados
- ✅ Respeta la estructura de carpetas
- ℹ️ Ejecuta tests opcionales (si pytest está instalado)

#### **Opción B: Compilar UN solo archivo**

```bash
.venv/bin/pyside6-uic --from-imports ui/frmempresas.ui -o modulos/empresas/view/ui_frmempresas.py

# Luego ejecutar los scripts de limpieza
.venv/bin/python scripts/ui_tools/remove_palette.py modulos/empresas/view/ui_frmempresas.py
.venv/bin/python scripts/ui_tools/fix_qt_constants.py modulos/empresas/view/ui_frmempresas.py
```

---

### 3️⃣ **Crear la clase View (súper simple)**

Crea un archivo `MiPantallaView.py` en el módulo correspondiente:

```python
# modulos/mi_modulo/view/MiPantallaView.py
from PySide6.QtWidgets import QDialog
from .ui_mi_pantalla import Ui_MiPantalla


class MiPantallaView(QDialog, Ui_MiPantalla):
    """Vista de Mi Pantalla - hereda estilos automáticamente del QSS global"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
```

**¡Y YA ESTÁ!** No necesitas:
- ❌ Heredar de `StyledWidget`
- ❌ Aplicar estilos manualmente
- ❌ Forzar `WA_StyledBackground`
- ❌ Llamar `setStyleSheet()` en cada widget

**Todo se hereda automáticamente del QSS global.**

---

## 🎨 **¿Por qué funciona ahora automáticamente?**

1. **QSS global aplicado en `main.py`:**
   ```python
   app.setStyleSheet(qss)  # Se aplica a TODA la aplicación
   ```

2. **QSS de Creative ERP copiado:**
   - Archivo: `styles.qss` (copiado de `Creative_ERP/resources/styles/modern.qss`)
   - Define estilos para: QLineEdit, QComboBox, QPushButton, QTabWidget, etc.

3. **Qt hereda estilos por jerarquía:**
   - Widgets hijos heredan automáticamente del padre
   - No necesitas código especial

---

## 📂 **Estructura de archivos recomendada**

```
modulos/
├── mi_modulo/
│   ├── __init__.py
│   ├── controller/
│   │   └── controller.py
│   ├── model/
│   │   └── model.py
│   └── view/
│       ├── ui_mi_pantalla.py     ← Generado automáticamente
│       └── MiPantallaView.py      ← Tu clase simple
ui/
└── mi_pantalla.ui                  ← Diseñado en Qt Designer
```

---

## ⚠️ **Errores comunes y soluciones**

### Error: "Unknown property content"
**Causa:** El QSS tiene propiedades CSS que Qt no reconoce.  
**Solución:** Ignorar, son warnings inofensivos.

### Error: "Cannot find reference to designer_rc"
**Causa:** El import del QRC está mal.  
**Solución:** El script `compile_ui.sh` lo corrige automáticamente.

### Los widgets se ven negros/sin estilo
**Causa:** El widget padre tiene un `setStyleSheet()` que bloquea la herencia.  
**Solución:** NO uses `setStyleSheet()` en contenedores (QFrame, QDialog, etc.). Usa clases CSS en su lugar.

---

## 🔧 **Actualizar el QSS global**

Si necesitas cambiar colores o estilos para **TODA la aplicación**:

```bash
# Editar el QSS
nano styles.qss

# NO necesitas recompilar nada, solo reiniciar la app
```

Los cambios se aplicarán a **todas las pantallas** automáticamente.

---

## 📝 **Ejemplo completo: Importar pantalla de Clientes**

```bash
# 1. Diseñar en Qt Designer
qtcreator ui/frmClientes.ui

# 2. Compilar
./scripts/compile_ui.sh

# 3. Crear la vista
cat > modulos/ventas/view/clientes_view.py << 'EOF'
from PySide6.QtWidgets import QDialog
from .ui_frmClientes import Ui_FrmClientes


class ClientesView(QDialog, Ui_FrmClientes):
    """Vista de gestión de clientes"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
EOF

# 4. Crear modelo y controlador (MVC completo)
# ... (tu lógica de negocio)

# 5. ¡Listo! Se ve exactamente como Creative ERP
```

---

## 🎯 **Resumen: ¿Se va a ir todo a la mierda?**

### ❌ **NO**

- Recompilar `.ui` a `.py` es **seguro y necesario**
- El QSS se aplica **automáticamente** a todos los widgets
- No necesitas código especial en cada vista
- Puedes importar **200-300 pantallas** sin drama

### ✅ **Lo único que necesitas:**

1. Diseñar en Qt Designer
2. Ejecutar `./scripts/compile_ui.sh`
3. Crear una clase View de 5 líneas
4. **¡Profit!** Se ve como Creative ERP

---

## 📞 **¿Problemas?**

Si una pantalla específica no se ve bien:

1. Verifica que NO tenga `setStyleSheet()` en el código Python
2. Verifica que el `.ui` no tenga colores hardcodeados (el script los limpia, pero revisa)
3. Verifica que los widgets sean estándar de Qt (QLineEdit, QComboBox, etc.)

**En el 99% de los casos, funcionará automáticamente.** 🎉

---

## 🧪 **Tests opcionales**

El script ejecuta tests automáticos si tienes `pytest` instalado:

```bash
# Instalar pytest (opcional, solo para desarrollo)
.venv/bin/pip install pytest

# Los tests verifican que todos los imports funcionen correctamente
```

Si no tienes `pytest`, el script simplemente omite los tests y compila todo correctamente.

