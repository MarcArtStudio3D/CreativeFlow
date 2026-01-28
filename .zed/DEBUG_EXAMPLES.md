# Ejemplos Prácticos de Debug para Creative Flow

## 🎯 Casos de Uso Comunes

Esta guía contiene ejemplos específicos de debugging para tu aplicación Creative Flow con Python Qt6.

---

## 📋 Tabla de Contenidos

1. [Debug del Proceso de Login](#1-debug-del-proceso-de-login)
2. [Debug de la Base de Datos](#2-debug-de-la-base-de-datos)
3. [Debug de Widgets Qt](#3-debug-de-widgets-qt)
4. [Debug de Señales y Slots](#4-debug-de-señales-y-slots)
5. [Debug del DataManager](#5-debug-del-datamanager)
6. [Debug de Errores de Conexión](#6-debug-de-errores-de-conexión)
7. [Debug de la Ventana Principal](#7-debug-de-la-ventana-principal)
8. [Debug de Estilos QSS](#8-debug-de-estilos-qss)

---

## 1. Debug del Proceso de Login

### Escenario: Usuario no puede iniciar sesión

**Archivo**: `login/controller.py`

#### Breakpoints recomendados:

```python
# login/controller.py - Línea ~28
def handle_login(self):
    datos = self.view.get_credentials()  # <- BREAKPOINT 1
    resultado = self.model.validar_acceso(
        datos['empresa'], 
        datos['usuario'], 
        datos['pass']
    )  # <- BREAKPOINT 2

    if resultado["success"]:  # <- BREAKPOINT 3
        session_data = {
            "id_empresa": self.model.get_empresa_id(datos['empresa']),
            # ...
        }
```

#### Pasos de debug:

1. Coloca breakpoint en `BREAKPOINT 1`
2. Inicia la aplicación (F5)
3. Ingresa credenciales en el formulario
4. Haz clic en "Login"
5. El debugger se detendrá en `datos = self.view.get_credentials()`
6. Inspecciona la variable `datos` para ver qué valores se capturaron:
   - `datos['empresa']`
   - `datos['usuario']`
   - `datos['pass']`
7. Usa F10 para avanzar a la validación
8. Inspecciona `resultado` para ver si `success` es True/False
9. Verifica `resultado["rol"]` si la autenticación fue exitosa

#### Variables clave a inspeccionar:

- `datos`: Diccionario con las credenciales ingresadas
- `resultado`: Diccionario con el resultado de la validación
- `session_data`: Datos de la sesión si login exitoso
- `self.model`: Instancia del modelo de datos

---

## 2. Debug de la Base de Datos

### Escenario: Queries SQL no devuelven resultados esperados

**Archivo**: `database/DataManager.py`

#### Breakpoints recomendados:

```python
# database/DataManager.py
def ejecutar_query(self, query, params=None):
    # <- BREAKPOINT: Inspecciona la query antes de ejecutar
    cursor = self.connection.cursor()
    
    if params:
        cursor.execute(query, params)  # <- BREAKPOINT con params
    else:
        cursor.execute(query)  # <- BREAKPOINT sin params
    
    resultado = cursor.fetchall()  # <- BREAKPOINT: Ver resultados
    return resultado
```

#### Pasos de debug:

1. Coloca breakpoint antes de `cursor.execute()`
2. Cuando se detenga, inspecciona:
   - `query`: La consulta SQL completa
   - `params`: Parámetros de la query (si existen)
   - `self.connection`: Estado de la conexión
3. Usa F10 para ejecutar la query
4. Inspecciona `resultado` después de `fetchall()`
5. Verifica `len(resultado)` para saber cuántos registros se obtuvieron

#### Tips:

- Copia el contenido de `query` desde el debugger
- Pruébalo directamente en DBeaver o cliente SQL
- Verifica que `params` contenga los valores esperados
- Comprueba que `self.connection` no sea None

---

## 3. Debug de Widgets Qt

### Escenario: Un widget no se muestra o tiene propiedades incorrectas

**Archivo**: `login/LoginScreen.py` o cualquier archivo de UI

#### Breakpoints recomendados:

```python
# En el constructor de tu widget
def __init__(self, controller):
    super().__init__()
    self.controller = controller
    self.setup_ui()  # <- BREAKPOINT 1
    self.apply_styles()  # <- BREAKPOINT 2
    
def setup_ui(self):
    # Configuración de widgets
    self.button = QPushButton("Login")  # <- BREAKPOINT 3
    self.button.setEnabled(True)
    self.layout.addWidget(self.button)  # <- BREAKPOINT 4
```

#### Pasos de debug:

1. Coloca breakpoint después de crear cada widget
2. Inspecciona las propiedades del widget:
   - `self.button.isEnabled()`
   - `self.button.isVisible()`
   - `self.button.text()`
   - `self.button.size()`
   - `self.button.geometry()`
3. Verifica que el widget esté agregado al layout correcto
4. Comprueba el parent del widget

#### Variables a inspeccionar:

- `self.button.parent()`: Debe tener un parent válido
- `self.layout`: El layout debe existir
- `self.isVisible()`: El widget contenedor debe ser visible

---

## 4. Debug de Señales y Slots

### Escenario: Un botón no responde al hacer clic

**Archivo**: Cualquier controlador o vista

#### Breakpoints recomendados:

```python
# Donde se conecta la señal
def setup_connections(self):
    self.button.clicked.connect(self.on_button_clicked)  # <- BREAKPOINT 1
    
def on_button_clicked(self):
    # <- BREAKPOINT 2: Aquí debería llegar al hacer clic
    print("Botón clickeado")
    self.procesar_datos()
```

#### Pasos de debug:

1. Coloca breakpoint en la conexión de la señal
2. Verifica que la conexión se realice correctamente
3. Coloca breakpoint dentro del slot (`on_button_clicked`)
4. Ejecuta la aplicación y haz clic en el botón
5. Si no llega al breakpoint del slot:
   - El botón no está conectado correctamente
   - El botón está deshabilitado (`isEnabled()` es False)
   - Hay otro widget encima capturando el clic

#### Verificaciones:

```python
# En la consola de debug, evalúa:
self.button.isEnabled()  # Debe ser True
self.button.receivers(SIGNAL("clicked()"))  # Debe ser > 0
```

---

## 5. Debug del DataManager

### Escenario: Problemas al cambiar de base de datos

**Archivo**: `database/DataManager.py`

#### Breakpoints recomendados:

```python
# main.py - Línea ~23
def main():
    # ...
    data_manager = DataManager()  # <- BREAKPOINT 1
    
# login/controller.py
def abrir_sistema_principal(self, session_data, db_config):
    # <- BREAKPOINT 2: Antes de cambiar de BD
    conectado = self.data_manager.conectar_a_empresa(db_config)
    
    if conectado:  # <- BREAKPOINT 3
        self.main_window = MainWindow(self.data_manager, session_data)
```

#### Pasos de debug:

1. Breakpoint en creación de DataManager
2. Inspecciona `data_manager.connection` (debe ser None inicialmente)
3. Breakpoint antes de `conectar_a_empresa()`
4. Inspecciona `db_config`:
   - `db_config['host']`
   - `db_config['database']`
   - `db_config['user']`
   - `db_config['password']`
   - `db_config['tipo_bd']`
5. Usa F11 para entrar en `conectar_a_empresa()`
6. Verifica el valor de retorno `conectado`

#### Variables clave:

- `self.data_manager.connection`: Estado de la conexión actual
- `self.data_manager.tipo_bd`: Tipo de BD conectada
- `db_config`: Configuración de conexión

---

## 6. Debug de Errores de Conexión

### Escenario: Error al conectar a PostgreSQL o MariaDB

**Archivo**: `database/DataManager.py`

#### Breakpoints recomendados:

```python
def conectar_a_empresa(self, db_config):
    try:
        # <- BREAKPOINT 1: Antes del intento de conexión
        if db_config['tipo_bd'] == 'postgresql':
            import psycopg2
            self.connection = psycopg2.connect(
                host=db_config['host'],
                database=db_config['database'],
                user=db_config['user'],
                password=db_config['password']
            )  # <- BREAKPOINT 2
        elif db_config['tipo_bd'] == 'mariadb':
            import mysql.connector
            # ...
            
        return True  # <- BREAKPOINT 3
        
    except Exception as e:
        # <- BREAKPOINT 4: Captura del error
        print(f"Error de conexión: {e}")
        return False
```

#### Pasos de debug:

1. Breakpoint antes del try
2. Inspecciona todos los valores de `db_config`
3. Si falla, el debugger se detendrá en el except
4. Inspecciona la excepción `e`:
   - `str(e)`: Mensaje de error
   - `type(e)`: Tipo de excepción
5. Verifica que los módulos estén importados (`psycopg2`, `mysql.connector`)

#### Errores comunes:

- **"Module not found"**: Falta instalar el driver
- **"Authentication failed"**: Usuario/contraseña incorrectos
- **"Connection refused"**: Host/puerto incorrectos
- **"Database does not exist"**: Nombre de BD incorrecto

---

## 7. Debug de la Ventana Principal

### Escenario: MainWindow no se abre después del login

**Archivo**: `MainWindow.py`

#### Breakpoints recomendados:

```python
# MainWindow.py
class MainWindow(QMainWindow):
    def __init__(self, data_manager, session_data):
        super().__init__()  # <- BREAKPOINT 1
        
        self.data_manager = data_manager
        self.session_data = session_data  # <- BREAKPOINT 2
        
        self.setup_ui()  # <- BREAKPOINT 3
        self.cargar_modulos()  # <- BREAKPOINT 4
        
    def setup_ui(self):
        # <- BREAKPOINT 5: Configuración de UI
        self.setWindowTitle("Creative Flow")
        self.setCentralWidget(self.central_widget)
```

#### Pasos de debug:

1. Breakpoint en `__init__`
2. Inspecciona los parámetros recibidos:
   - `data_manager`: No debe ser None
   - `session_data`: Debe contener todos los campos necesarios
3. Avanza con F10 por cada método de inicialización
4. Si falla en algún punto, usa F11 para entrar en ese método
5. Verifica que `self.show()` se llame al final

#### Variables clave:

- `self.data_manager.connection`: Debe estar conectado
- `self.session_data['empresa']`: Nombre de la empresa
- `self.session_data['usuario']`: Usuario logueado
- `self.session_data['rol']`: Rol del usuario

---

## 8. Debug de Estilos QSS

### Escenario: Los estilos CSS no se aplican correctamente

**Archivo**: `main.py`

#### Breakpoints recomendados:

```python
# main.py
def aplicar_estilo_personalizado(app):
    style_path = "styles.qss"  # <- BREAKPOINT 1
    
    if os.path.exists(style_path):  # <- BREAKPOINT 2
        with open(style_path, "r", encoding="utf-8") as f:
            stylesheet = f.read()  # <- BREAKPOINT 3
            app.setStyleSheet(stylesheet)
        print(f"✓ Estilos cargados desde {style_path}")
    else:
        print(f"✗ No se encontró {style_path}")  # <- BREAKPOINT 4
```

#### Pasos de debug:

1. Verifica que `style_path` sea correcto
2. Comprueba que `os.path.exists()` retorne True
3. Inspecciona el contenido de `stylesheet`
4. Si el archivo no existe, verifica la ruta actual:
   ```python
   os.getcwd()  # Ver directorio actual
   os.path.abspath(style_path)  # Ruta absoluta
   ```

#### Verificaciones adicionales:

- El archivo `styles.qss` existe en el directorio raíz
- El archivo tiene la codificación correcta (UTF-8)
- No hay errores de sintaxis en el QSS
- Los selectores QSS son correctos (QPushButton, QLabel, etc.)

---

## 🎓 Ejemplo Completo: Debug de Login a MainWindow

### Flujo completo de debug:

```plaintext
1. main.py:23 - Creación de DataManager
   ├─ Inspeccionar: data_manager
   └─ Verificar: connection = None

2. login/controller.py:13 - Inicialización de LoginController
   ├─ Inspeccionar: self.data_manager
   └─ Verificar: self.model se crea correctamente

3. login/controller.py:28 - handle_login()
   ├─ Inspeccionar: datos (credenciales)
   └─ Verificar: datos['empresa'], datos['usuario'], datos['pass']

4. login/model.py - validar_acceso()
   ├─ Inspeccionar: query SQL
   └─ Verificar: resultado["success"], resultado["rol"]

5. login/controller.py:45 - verificar_existencia_bd_empresa()
   ├─ Inspeccionar: db_config
   └─ Verificar: existe_bd = True

6. database/DataManager.py - conectar_a_empresa()
   ├─ Inspeccionar: db_config
   └─ Verificar: connection establecida

7. MainWindow.py:10 - Inicialización de MainWindow
   ├─ Inspeccionar: data_manager.connection
   ├─ Inspeccionar: session_data
   └─ Verificar: MainWindow se crea y muestra
```

### Comando para cada paso:

- **F10**: Step Over - Avanzar a la siguiente línea
- **F11**: Step Into - Entrar en la función
- **Shift+F11**: Step Out - Salir de la función actual
- **F5**: Continue - Continuar hasta el siguiente breakpoint

---

## 💡 Tips Avanzados

### 1. Evaluación de expresiones

Durante debug, puedes evaluar expresiones Python en la consola:

```python
# Ver estructura completa de un objeto
vars(self)

# Ver todos los atributos
dir(self.data_manager)

# Verificar tipo
type(self.connection)

# Ver si un método existe
hasattr(self, 'metodo_nombre')
```

### 2. Breakpoints condicionales

En algunos debuggers puedes crear breakpoints condicionales:

```python
# Solo pausar si usuario es 'admin'
# Breakpoint condition: datos['usuario'] == 'admin'
```

### 3. Watch expressions

Agrega expresiones para monitorear constantemente:

- `self.data_manager.connection`
- `self.session_data['usuario']`
- `len(self.widgets_list)`

### 4. Log points

En lugar de breakpoints, puedes agregar prints temporales:

```python
import logging
logging.debug(f"Variable x = {x}, y = {y}")
```

---

## 📚 Recursos Relacionados

- **[DEBUG_GUIDE.md](DEBUG_GUIDE.md)** - Guía completa del debugger
- **[README.md](README.md)** - Configuración de Zed
- **[test_debug.py](test_debug.py)** - Script de prueba

---

## ✅ Checklist de Debug

Antes de empezar a debuggear:

- [ ] Guarda todos los archivos modificados
- [ ] Verifica que el entorno virtual esté activo
- [ ] Comprueba que debugpy esté instalado
- [ ] Identifica el punto exacto donde ocurre el problema
- [ ] Coloca breakpoints estratégicamente
- [ ] Ten a mano la documentación de Qt6/PySide6

Durante el debug:

- [ ] Inspecciona variables antes y después de cada operación
- [ ] Verifica valores de retorno de funciones
- [ ] Comprueba el flujo de ejecución (if/else)
- [ ] Revisa que los objetos no sean None
- [ ] Verifica el contenido de listas y diccionarios

Después del debug:

- [ ] Documenta el problema y la solución
- [ ] Elimina breakpoints innecesarios
- [ ] Limpia prints de debug
- [ ] Verifica que la solución funcione en todos los casos

---

**Happy Debugging! 🐛🔍**

_Última actualización: 27 de enero, 2025_