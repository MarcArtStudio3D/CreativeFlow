# Guía de Debug en Zed para Creative Flow

## 🎯 Configuración Completada

El debugger de Zed está configurado para depurar tu aplicación Python Qt6 con las siguientes características:

### ✅ Configuración Actual

- **Debugger**: `debugpy` (ya instalado en tu `.venv`)
- **Archivo principal**: `main.py`
- **Python**: `/home/marc/Artstudio3D/CreativeFlow/.venv/bin/python`
- **Variables de entorno Qt6** configuradas automáticamente

## 🚀 Cómo Usar el Debugger

### 1. Iniciar Debug

Tienes varias opciones para iniciar el debug:

- **Método 1**: Presiona `F5` (configurado en keymap)
- **Método 2**: Abre la paleta de comandos (`Ctrl+Shift+P`) y busca "Debug: Start"
- **Método 3**: Haz clic en el botón de debug en la interfaz de Zed

### 2. Establecer Breakpoints

Para establecer un punto de interrupción:

- **Método 1**: Presiona `F9` en la línea donde quieres pausar la ejecución
- **Método 2**: Haz clic en el margen izquierdo del editor (donde aparecen los números de línea)

**Ejemplo**: Si quieres debuggear el inicio de la aplicación, coloca un breakpoint en `main.py` en la línea:

```python
app = QApplication(sys.argv)
```

### 3. Controles de Navegación Durante Debug

Una vez que el debugger se detiene en un breakpoint:

- **F10** (`Step Over`): Ejecuta la línea actual y avanza a la siguiente
- **F11** (`Step Into`): Entra dentro de la función en la línea actual
- **Shift+F11** (`Step Out`): Sale de la función actual
- **F5** (`Continue`): Continúa la ejecución hasta el siguiente breakpoint
- **Shift+F5** (`Stop`): Detiene la sesión de debug

### 4. Inspeccionar Variables

Cuando el debugger está pausado:

- Las variables locales aparecen en el panel de debug
- Puedes ver el valor de cualquier variable en el scope actual
- Puedes expandir objetos complejos para ver sus propiedades

## 🎨 Debug de Qt6

### Variables de Entorno Configuradas

El debugger está configurado con variables específicas para Qt6:

- `QT_LOGGING_RULES`: Reduce warnings innecesarios de SQL
- `QT_QPA_PLATFORM`: Forzado a `xcb` para Linux
- `PYTHONPATH`: Configurado al workspace

### Lugares Comunes para Breakpoints

1. **En `main.py`**:
   - Línea de `app = QApplication(sys.argv)` - Inicio de la app
   - Línea de `data_manager = DataManager()` - Inicialización de DB
   - Línea de `login_ctrl = LoginController(data_manager)` - Inicio del login

2. **En `MainWindow.py`**:
   - Constructor `__init__`
   - Métodos de inicialización de UI
   - Slots conectados a señales

3. **En controladores**:
   - Métodos que manejan eventos de botones
   - Validaciones de datos
   - Consultas a la base de datos

## 🔧 Opciones Avanzadas

### Modificar Configuración

El archivo de configuración está en `.zed/debug.json`. Puedes modificar:

#### Agregar argumentos de línea de comandos:

```json
"args": ["--verbose", "--debug"]
```

#### Modificar variables de entorno:

```json
"env": {
  "QT_LOGGING_RULES": "qt.sql.qsqldatabase.warning=false",
  "PYTHONPATH": "${workspaceFolder}",
  "QT_QPA_PLATFORM": "xcb",
  "DEBUG_MODE": "true"
}
```

#### Cambiar opciones de debug:

```json
"justMyCode": false,     // false = debuggear también librerías externas
"stopOnEntry": true,     // true = pausar al inicio del programa
```

## 📝 Tips y Trucos

### 1. Debug de Widgets Qt

Para inspeccionar widgets Qt durante debug:

```python
# Coloca breakpoints después de crear widgets
button = QPushButton("Click me")
# <- breakpoint aquí para inspeccionar el botón
```

### 2. Debug de Señales y Slots

```python
# En tu código, agrega breakpoints en los métodos conectados
def on_button_clicked(self):
    # <- breakpoint aquí
    print("Button clicked")
```

### 3. Debug de Base de Datos

```python
# En DataManager o métodos de DB
def execute_query(self, query):
    # <- breakpoint aquí para ver la query antes de ejecutarla
    cursor = self.connection.cursor()
    cursor.execute(query)
```

### 4. Evaluar Expresiones

Durante una sesión de debug, puedes evaluar expresiones Python en la consola de debug:

- Consultar valores: `print(variable_name)`
- Ejecutar código: `some_function()`
- Modificar variables temporalmente: `variable_name = new_value`

## ⚠️ Solución de Problemas

### El debugger no se inicia

1. Verifica que `debugpy` esté instalado:
   ```bash
   .venv/bin/pip list | grep debugpy
   ```

2. Si no está instalado:
   ```bash
   .venv/bin/pip install debugpy
   ```

### La aplicación Qt no se muestra

Si la ventana Qt no aparece durante debug:

1. Verifica que `QT_QPA_PLATFORM` esté configurado correctamente
2. En algunos entornos puede necesitar `wayland` en lugar de `xcb`

### Breakpoints no funcionan

1. Asegúrate de guardar el archivo antes de iniciar debug
2. Verifica que el archivo esté en el PYTHONPATH
3. Intenta establecer el breakpoint en una línea con código ejecutable (no en líneas en blanco o comentarios)

## 🎓 Ejemplo de Sesión de Debug

### Scenario: Debuggear el proceso de login

1. Abre `login/controller.py`
2. Encuentra el método que valida el usuario (por ejemplo `validate_user()`)
3. Coloca un breakpoint en la primera línea del método (F9)
4. Inicia el debugger (F5)
5. La aplicación se abrirá normalmente
6. Ingresa usuario y contraseña y haz clic en "Login"
7. El debugger se detendrá en tu breakpoint
8. Usa F10 para avanzar línea por línea
9. Inspecciona las variables `username`, `password`, etc.
10. Usa F5 para continuar la ejecución

## 📚 Recursos Adicionales

- Documentación de debugpy: https://github.com/microsoft/debugpy
- Documentación de Zed Debugger: https://zed.dev/docs/debugging
- Qt6 Debugging Tips: https://doc.qt.io/qt-6/debug.html

---

**¡Happy Debugging! 🐛**