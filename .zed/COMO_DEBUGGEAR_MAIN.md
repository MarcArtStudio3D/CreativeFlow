# 🎯 Cómo Debuggear desde main.py (Solución al Problema)

## ❌ El Problema

Cuando presionas **F5** en Zed, te muestra varias opciones como:
- `run module '...lientesModel.py'`
- `pytest '...lientesModel.py'`
- `pytest modulos/ventas/model/ClientesModel.py`
- `run '...lientesModel.py'`

Estas opciones **NO SIRVEN** porque intentan ejecutar el archivo actual, pero tu aplicación Qt6 **DEBE iniciarse desde `main.py`** para que todo el contexto (DataManager, sesión, login, etc.) esté disponible.

---

## ✅ La Solución

Ahora tienes **4 configuraciones de debug** disponibles. Debes seleccionar la primera.

### Paso a Paso:

1. **Abre cualquier archivo** en tu proyecto (por ejemplo, `login/controller.py` o `MainWindow.py`)

2. **Coloca breakpoints** donde quieras debuggear:
   - Haz clic en el margen izquierdo (donde están los números de línea)
   - O presiona **F9** en la línea deseada
   - Aparecerá un punto rojo 🔴

3. **Presiona F5**

4. **Selecciona la primera opción**:
   ```
   🚀 Debug Creative Flow - MAIN APPLICATION
   ```

5. La aplicación se iniciará desde `main.py` y se detendrá en tus breakpoints

---

## 📋 Configuraciones Disponibles

Cuando presiones **F5**, verás estas opciones en el menú de debug:

### 1. 🚀 Debug Creative Flow - MAIN APPLICATION ⭐ **USA ESTA**
- **Inicia desde**: `main.py`
- **Uso**: Debug normal de la aplicación completa
- **Cuándo usarla**: Siempre que quieras debuggear tu app Qt6
- **Breakpoints**: Funcionan en cualquier archivo del proyecto

### 2. ▶️ Run Creative Flow (No Debug)
- **Inicia desde**: `main.py`
- **Uso**: Ejecuta la app sin debugger (más rápido)
- **Cuándo usarla**: Para probar cambios rápidos sin debugging

### 3. 🔍 Debug Current File
- **Inicia desde**: El archivo actualmente abierto
- **Uso**: Para scripts standalone que no necesitan main.py
- **Cuándo usarla**: Solo para archivos independientes
- **⚠️ NO USES ESTO para tu app Qt6**

### 4. 🧪 Debug with Pytest
- **Inicia desde**: Pytest en el archivo actual
- **Uso**: Para ejecutar tests unitarios
- **Cuándo usarla**: Solo cuando estés en un archivo de tests

---

## 🎯 Ejemplo Práctico: Debug del Login

Imagina que quieres debuggear el proceso de login:

### Sin hacer nada especial:

1. **Abre** `login/controller.py`

2. **Busca** el método `handle_login` (línea ~28)

3. **Coloca breakpoint** en esta línea:
   ```python
   def handle_login(self):
       datos = self.view.get_credentials()  # <- Haz clic aquí en el margen
   ```

4. **Presiona F5**

5. **Selecciona**: `🚀 Debug Creative Flow - MAIN APPLICATION`

6. **Se abrirá** la ventana de login

7. **Ingresa** usuario y contraseña

8. **Haz clic** en "Login"

9. **El debugger se detendrá** en tu breakpoint 🎉

10. **Inspecciona** las variables:
    - `self.view`
    - `datos`
    - `self.model`

11. **Navega** con:
    - **F10** → Siguiente línea
    - **F11** → Entrar en función
    - **F5** → Continuar hasta siguiente breakpoint

---

## 🔍 Por Qué Funciona Ahora

### Antes (❌ No funcionaba):
```
Archivo abierto: login/controller.py
Presionas F5 → Intenta ejecutar login/controller.py directamente
Resultado: ERROR - No hay QApplication, no hay DataManager, etc.
```

### Ahora (✅ Funciona):
```
Archivo abierto: login/controller.py (con breakpoints)
Presionas F5 → Seleccionas "Debug Creative Flow - MAIN APPLICATION"
Zed ejecuta: main.py (que inicializa todo correctamente)
Tu breakpoint en login/controller.py: ¡Se activa cuando llegue ahí!
Resultado: ✓ Debug funciona perfectamente
```

---

## 💡 Flujo de Ejecución

Cuando seleccionas "Debug Creative Flow - MAIN APPLICATION":

```
1. Se ejecuta main.py
   ├─ Crea QApplication
   ├─ Inicializa DataManager
   ├─ Carga estilos
   └─ Abre LoginController
   
2. LoginController se muestra
   └─ Usuario hace login
   
3. Se llama a handle_login()
   └─ 🔴 BREAKPOINT AQUÍ (si lo colocaste)
   
4. Debugger se detiene
   └─ Puedes inspeccionar todo
```

---

## 🎨 Breakpoints en Diferentes Archivos

Puedes tener breakpoints en múltiples archivos al mismo tiempo:

```python
# main.py - Línea 23
app = QApplication(sys.argv)  # <- Breakpoint 1

# login/controller.py - Línea 28
datos = self.view.get_credentials()  # <- Breakpoint 2

# database/DataManager.py
def conectar_a_empresa(self, db_config):  # <- Breakpoint 3
    # ...

# MainWindow.py
def __init__(self, data_manager, session_data):  # <- Breakpoint 4
    # ...
```

Presionas **F5** → Seleccionas "Debug Creative Flow" → Todos los breakpoints funcionarán 🎉

---

## ⚠️ Errores Comunes

### ❌ Error 1: Seleccionar la configuración incorrecta

```
Síntoma: La app no inicia o da errores de importación
Causa: Seleccionaste "run module" o "Debug Current File"
Solución: Usa "🚀 Debug Creative Flow - MAIN APPLICATION"
```

### ❌ Error 2: Breakpoints en gris (no funcionan)

```
Síntoma: Los breakpoints aparecen en gris y no se detienen
Causa: No guardaste el archivo
Solución: Presiona Ctrl+S para guardar antes de debuggear
```

### ❌ Error 3: No llega al breakpoint

```
Síntoma: La app se ejecuta pero nunca se detiene en tu breakpoint
Causa: Esa línea de código no se ejecuta
Solución: 
  1. Verifica que el flujo de ejecución llegue a esa línea
  2. Pon un breakpoint antes para confirmar el flujo
  3. Revisa condiciones if/else que puedan saltarse el código
```

---

## 🚀 Script Alternativo (Método Manual)

Si Zed no muestra las configuraciones correctamente, puedes ejecutar manualmente:

```bash
# Desde el directorio del proyecto
cd /home/marc/Artstudio3D/CreativeFlow

# Ejecutar con debugger
.venv/bin/python -m debugpy --listen 5678 --wait-for-client main.py
```

O usar el script que creé:

```bash
.zed/debug_main.sh
```

---

## 📊 Comparación: PyCharm vs Zed

| Característica | PyCharm | Zed |
|----------------|---------|-----|
| **Inicio de debug** | Botón Run/Debug | F5 → Seleccionar config |
| **Configuración** | Automática | Manual (ya hecha ✓) |
| **Breakpoints** | Automáticos | Automáticos |
| **Inspección** | Panel derecho | Panel de variables |
| **Step Over** | F8 | F10 |
| **Step Into** | F7 | F11 |

**La diferencia principal**: En Zed debes **seleccionar la configuración** correcta del menú.

---

## ✅ Checklist de Debug

Antes de debuggear:

- [ ] Has guardado todos los archivos modificados (Ctrl+S)
- [ ] Has colocado breakpoints en las líneas correctas
- [ ] Sabes qué variables quieres inspeccionar
- [ ] Has identificado el flujo de ejecución

Durante el debug:

- [ ] Has presionado F5
- [ ] Has seleccionado "🚀 Debug Creative Flow - MAIN APPLICATION"
- [ ] La ventana de la app se ha abierto
- [ ] Has realizado las acciones necesarias para llegar a tu breakpoint
- [ ] El debugger se ha detenido en tu breakpoint

Si algo falla:

- [ ] Verifica que debugpy esté instalado: `.venv/bin/pip list | grep debugpy`
- [ ] Comprueba que los archivos JSON no tengan errores de sintaxis
- [ ] Revisa los logs en la terminal integrada de Zed
- [ ] Consulta `DEBUG_GUIDE.md` para más ayuda

---

## 🎓 Resumen

**Para debuggear tu aplicación Qt6 en Zed:**

1. ✅ Coloca breakpoints donde quieras
2. ✅ Presiona **F5**
3. ✅ Selecciona **"🚀 Debug Creative Flow - MAIN APPLICATION"**
4. ✅ Usa la aplicación normalmente
5. ✅ El debugger se detendrá en tus breakpoints
6. ✅ Inspecciona variables y navega con F10/F11

**¡Así de simple!** 🎉

---

## 📚 Más Información

- **DEBUG_GUIDE.md** - Guía completa de debugging
- **DEBUG_EXAMPLES.md** - Ejemplos prácticos específicos
- **INICIO_RAPIDO.md** - Guía de inicio rápido
- **README.md** - Información general de configuración

---

_Última actualización: 27 de enero, 2025_
_Si tienes problemas, consulta los otros archivos de documentación en `.zed/`_