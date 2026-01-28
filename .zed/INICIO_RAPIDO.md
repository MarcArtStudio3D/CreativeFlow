# 🚀 Inicio Rápido - Debug en Zed

## ⚡ Empezar en 3 Pasos

### 1️⃣ Verifica la instalación
```bash
cd /home/marc/Artstudio3D/CreativeFlow
.venv/bin/pip list | grep debugpy
```

✅ Deberías ver: `debugpy 1.8.19` (o superior)

### 2️⃣ Prueba la configuración
```bash
.venv/bin/python .zed/test_debug.py
```

✅ Deberías ver todos los tests pasando con ✓

### 3️⃣ Empieza a debuggear

1. **Abre `main.py`** en Zed
2. **Coloca un breakpoint**: Haz clic en el margen izquierdo (donde están los números de línea) en la línea 23:
   ```python
   app = QApplication(sys.argv)  # <- clic aquí
   ```
3. **Inicia el debug**: Presiona `F5`
4. **La app se detendrá** en tu breakpoint
5. **Navega por el código**:
   - `F10` → Siguiente línea
   - `F11` → Entrar en función
   - `F5` → Continuar
   - `Shift+F5` → Detener

---

## 🎯 Lugares Útiles para Breakpoints

### Login
```python
# login/controller.py - Línea ~28
def handle_login(self):
    datos = self.view.get_credentials()  # <- breakpoint aquí
```

### Base de Datos
```python
# database/DataManager.py
def conectar_a_empresa(self, db_config):
    # <- breakpoint aquí para ver la config
```

### Ventana Principal
```python
# MainWindow.py
def __init__(self, data_manager, session_data):
    super().__init__()  # <- breakpoint aquí
```

---

## ⌨️ Atajos de Teclado

| Tecla | Acción |
|-------|--------|
| `F5` | Iniciar/Continuar |
| `F9` | Agregar/Quitar Breakpoint |
| `F10` | Siguiente Línea |
| `F11` | Entrar en Función |
| `Shift+F11` | Salir de Función |
| `Shift+F5` | Detener Debug |

---

## 🔍 Inspeccionar Variables

Cuando el debugger está pausado:

1. **Panel de Variables**: Mira el panel izquierdo/derecho de Zed
2. **Variables Locales**: Verás todas las variables del scope actual
3. **Expandir Objetos**: Haz clic en la flecha para ver propiedades
4. **Evaluar Expresiones**: Usa la consola de debug

### Ejemplos de qué inspeccionar:

```python
# En handle_login():
datos           # {'empresa': 'MiEmpresa', 'usuario': 'admin', ...}
resultado       # {'success': True, 'rol': 'administrador'}
session_data    # {'id_empresa': 1, 'empresa': 'MiEmpresa', ...}

# En DataManager:
self.connection      # Objeto de conexión activa
db_config           # {'host': 'localhost', 'database': ...}

# En MainWindow:
self.data_manager   # Instancia del gestor de datos
self.session_data   # Datos de la sesión actual
```

---

## 🐛 Ejemplo: Debuggear el Login

### Paso a paso:

1. Abre `login/controller.py`
2. Busca el método `handle_login(self)` (línea ~28)
3. Coloca breakpoints en:
   ```python
   def handle_login(self):
       datos = self.view.get_credentials()     # <- breakpoint 1
       resultado = self.model.validar_acceso(  # <- breakpoint 2
           datos['empresa'], 
           datos['usuario'], 
           datos['pass']
       )
       if resultado["success"]:                # <- breakpoint 3
   ```
4. Presiona `F5` para iniciar
5. En la ventana de login, ingresa usuario y contraseña
6. Haz clic en "Login"
7. El debugger se detendrá en breakpoint 1
8. Inspecciona `datos` en el panel de variables
9. Presiona `F10` para avanzar
10. Inspecciona `resultado` después de la validación
11. Presiona `F5` para continuar

---

## 🆘 Solución Rápida de Problemas

### ❌ El debugger no inicia

```bash
# Reinstala debugpy
.venv/bin/pip install --upgrade debugpy
```

### ❌ Los breakpoints aparecen en gris (no funcionan)

1. Guarda el archivo (`Ctrl+S`)
2. Verifica que estés en el archivo correcto
3. Coloca el breakpoint en una línea con código (no en líneas vacías)

### ❌ La ventana Qt no aparece

1. Verifica que uses el display correcto
2. En `debug.json` prueba cambiar:
   ```json
   "QT_QPA_PLATFORM": "wayland"  // en lugar de "xcb"
   ```

### ❌ "Module not found: debugpy"

```bash
# Activa el venv e instala
source .venv/bin/activate
pip install debugpy
```

---

## 📚 Más Información

- **README.md** → Resumen de la configuración
- **DEBUG_GUIDE.md** → Guía completa y detallada
- **DEBUG_EXAMPLES.md** → Ejemplos prácticos específicos
- **test_debug.py** → Script para probar la configuración

---

## 💡 Tips Rápidos

### ✨ Tip 1: Variables de Watch
Agrega expresiones para monitorear:
- `self.data_manager.connection`
- `session_data['usuario']`
- `len(lista_items)`

### ✨ Tip 2: Conditional Breakpoints
Algunos debuggers permiten breakpoints condicionales:
```python
# Solo pausar si usuario == 'admin'
```

### ✨ Tip 3: Logs durante Debug
Agrega prints temporales:
```python
print(f"🔍 DEBUG: variable = {variable}")
```

### ✨ Tip 4: Evalúa en la Consola
Durante el debug, prueba en la consola:
```python
type(self.connection)
vars(self)
dir(objeto)
```

---

## ✅ Checklist Pre-Debug

- [ ] Todos los archivos guardados
- [ ] Entorno virtual activo
- [ ] debugpy instalado
- [ ] Breakpoints colocados
- [ ] Sabes qué quieres inspeccionar

---

## 🎓 Workflow Recomendado

1. **Identifica el problema** → ¿Dónde ocurre?
2. **Coloca breakpoints** → Antes del problema
3. **Inicia debug** → Presiona F5
4. **Inspecciona variables** → ¿Qué valores tienen?
5. **Avanza paso a paso** → F10/F11
6. **Encuentra la causa** → ¿Dónde falla?
7. **Corrige el código** → Soluciona el bug
8. **Verifica** → Debug de nuevo para confirmar

---

**¡Listo para debuggear! 🐛🔍**

_Si tienes dudas, consulta los otros documentos en `.zed/`_