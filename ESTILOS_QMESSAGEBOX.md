# Sistema de Estilos Automáticos para QMessageBox

## 📋 Descripción

Este sistema aplica **automáticamente** estilos diferenciados a todos los QMessageBox de la aplicación sin necesidad de modificar cada controller.

## 🎨 Colores por Tipo de Mensaje

| Tipo | Color | Uso |
|------|-------|-----|
| **Warning** | 🔴 Rojo oscuro (#4d1f1f) | Advertencias, validaciones fallidas |
| **Critical** | 🔴 Rojo intenso (#5d0f0f) | Errores graves, fallos críticos |
| **Information** | 🔵 Azul oscuro (#1f2d4d) | Mensajes de éxito, confirmaciones |
| **Question** | 🟡 Amarillo/naranja (#4d3d1f) | Preguntas de confirmación |

## 🚀 Cómo Funciona

### 1. **Interceptor Global** (`helpers/messagebox_styles.py`)

La clase `MessageBoxStyler` actúa como un **event filter** que intercepta todos los QMessageBox antes de que se muestren y les aplica el estilo correspondiente según su icono.

### 2. **Activación en `main.py`**

```python
from helpers.messagebox_styles import MessageBoxStyler

# Instalar el interceptor global
messagebox_styler = MessageBoxStyler()
app.installEventFilter(messagebox_styler)
```

### 3. **Uso en Controllers** (Automático)

No necesitas hacer nada especial. Simplemente usa QMessageBox normalmente:

```python
# ✅ Warning (rojo)
QMessageBox.warning(self.view, "Título", "Mensaje de advertencia")

# ✅ Critical (rojo intenso)
QMessageBox.critical(self.view, "Título", "Error crítico")

# ✅ Information (azul)
QMessageBox.information(self.view, "Título", "Operación exitosa")

# ✅ Question (amarillo/naranja)
QMessageBox.question(self.view, "Título", "¿Estás seguro?")
```

O con instancias manuales:

```python
msg_box = QMessageBox(self.view)
msg_box.setIcon(QMessageBox.Warning)  # El color se aplica automáticamente
msg_box.setWindowTitle("Título")
msg_box.setText("Mensaje")
msg_box.exec()
```

## 🔧 Personalización

Si necesitas modificar los colores, edita el diccionario `ESTILOS` en `helpers/messagebox_styles.py`:

```python
ESTILOS = {
    QMessageBox.Warning: {
        "bg": "#4d1f1f",      # Color de fondo
        "text": "#ffdddd",    # Color del texto
        "btn_bg": "#8b0000",  # Color de fondo del botón
        # ... etc
    }
}
```

## 📦 Ventajas

✅ **Centralizado**: Un solo lugar para gestionar estilos  
✅ **Automático**: No modificas controllers existentes  
✅ **Escalable**: Funciona para las 200+ pantallas de la aplicación  
✅ **Consistente**: Todos los mensajes tienen el mismo look & feel  
✅ **Mantenible**: Cambios globales desde un solo archivo  

## 🔄 Compatibilidad Legacy

Se mantiene la función `aplicar_estilo_messagebox()` para compatibilidad con código existente, pero ya no es necesaria.

## 📝 Ejemplos

### Antes (manual en cada controller):
```python
msg_box = QMessageBox(self.view)
msg_box.setIcon(QMessageBox.Warning)
msg_box.setWindowTitle("Error")
msg_box.setText("Mensaje")
# ❌ Tenías que aplicar estilos manualmente
aplicar_estilo_messagebox(msg_box, "warning")
msg_box.exec()
```

### Ahora (automático):
```python
msg_box = QMessageBox(self.view)
msg_box.setIcon(QMessageBox.Warning)
msg_box.setWindowTitle("Error")
msg_box.setText("Mensaje")
# ✅ El estilo se aplica automáticamente
msg_box.exec()
```

O incluso más simple:
```python
# ✅ Una línea, estilo automático
QMessageBox.warning(self.view, "Error", "Mensaje")
```

## 🎯 Resultado

Todos los QMessageBox de la aplicación (login, empresas, ventas, almacén, etc.) tendrán colores diferenciados automáticamente sin tocar ningún controller. 🚀

