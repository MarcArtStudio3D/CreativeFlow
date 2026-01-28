# 🐛 Guía Rápida de Debug en Zed

## ⚡ Inicio Rápido (3 pasos)

1. **Coloca breakpoints** (clic en el margen izquierdo o F9)
2. **Presiona F5**
3. **Selecciona**: `🚀 Debug Creative Flow`

¡Eso es todo! 🎉

---

## 🎯 Problema Actual: No Aparece la Opción de Debug

Si cuando presionas **F5** no ves la opción `🚀 Debug Creative Flow`, sigue estos pasos:

### Solución 1: Reiniciar Zed

1. Cierra **completamente** Zed (Ctrl+Q)
2. Abre Zed de nuevo
3. Abre el proyecto CreativeFlow
4. Presiona F5
5. Deberías ver ahora las opciones de debug

### Solución 2: Verificar que debugpy esté instalado

```bash
cd /home/marc/Artstudio3D/CreativeFlow
source .venv/bin/activate
pip list | grep debugpy
```

Si no está instalado:
```bash
pip install debugpy
```

### Solución 3: Usar el Script Manual

Si Zed aún no muestra las opciones, usa el script de debug manual:

```bash
cd /home/marc/Artstudio3D/CreativeFlow
.zed/debug_main.sh
```

Este script:
- Activa el entorno virtual
- Inicia debugpy en el puerto 5678
- Ejecuta main.py
- Espera conexión del debugger

Luego en Zed:
1. Presiona F5
2. Selecciona "Python: Attach" si aparece
3. O conecta manualmente al puerto 5678

---

## 🔧 Verificar Configuración

### Revisar que los archivos JSON estén correctos:

```bash
cd /home/marc/Artstudio3D/CreativeFlow

# Verificar settings.json
python -m json.tool .zed/settings.json > /dev/null && echo "✓ OK" || echo "✗ ERROR"

# Verificar launch.json
python -m json.tool .zed/launch.json > /dev/null && echo "✓ OK" || echo "✗ ERROR"
```

Ambos deben mostrar `✓ OK`

---

## 🎮 Atajos de Teclado

Durante el debug:

| Tecla | Acción |
|-------|--------|
| **F5** | Continuar / Iniciar debug |
| **F9** | Colocar/quitar breakpoint |
| **F10** | Step Over (siguiente línea) |
| **F11** | Step Into (entrar en función) |
| **Shift+F11** | Step Out (salir de función) |
| **Shift+F5** | Detener debug |

---

## 📋 Ejemplo Práctico

Vamos a debuggear el login:

1. **Abre** `login/controller.py`

2. **Busca** el método `handle_login` (aproximadamente línea 28)

3. **Haz clic** en el margen izquierdo junto a esta línea:
   ```python
   def handle_login(self):
       datos = self.view.get_credentials()  # <- CLIC AQUÍ
   ```
   Aparecerá un punto rojo 🔴

4. **Guarda** el archivo (Ctrl+S)

5. **Presiona F5**

6. **Selecciona** `🚀 Debug Creative Flow`

7. **Espera** a que se abra la ventana de login

8. **Ingresa** usuario y contraseña

9. **Haz clic** en "Login"

10. **¡BOOM!** El debugger se detendrá en tu breakpoint 🎯

11. **Inspecciona** las variables en el panel de debug

---

## ❌ Problemas Comunes

### Problema: "No se detiene en mi breakpoint"

**Posibles causas:**
- El código no se está ejecutando (verifica el flujo)
- No guardaste el archivo (Ctrl+S)
- El breakpoint está en una línea vacía o comentario

**Solución:**
- Pon un breakpoint anterior para confirmar el flujo
- Asegúrate de guardar todos los archivos
- Mueve el breakpoint a una línea con código ejecutable

### Problema: "La aplicación no inicia"

**Posibles causas:**
- No estás usando la configuración correcta
- El entorno virtual no está activado
- Hay errores en el código

**Solución:**
- Asegúrate de seleccionar `🚀 Debug Creative Flow`
- Verifica que `.venv/bin/python` exista
- Revisa los logs en la terminal de Zed

### Problema: "No veo las opciones de debug"

**Posibles causas:**
- Zed no ha cargado la configuración
- Los archivos JSON tienen errores de sintaxis
- El plugin de Python no está activo

**Solución:**
- Reinicia Zed completamente
- Verifica los archivos JSON (ver sección anterior)
- Usa el script manual `.zed/debug_main.sh`

---

## 🚀 Alternativa: Debug desde Terminal

Si Zed no coopera, puedes debuggear desde la terminal:

```bash
cd /home/marc/Artstudio3D/CreativeFlow

# Ejecutar con debugpy
.venv/bin/python -m debugpy --listen 5678 --wait-for-client main.py
```

Esto:
1. Inicia el servidor de debug en el puerto 5678
2. Espera que un debugger se conecte
3. Una vez conectado, ejecuta main.py

Ventaja: Funciona siempre, sin depender de la configuración de Zed

---

## 📊 Estado del Proyecto

### ✅ Lo que YA está configurado:

- [x] `debugpy` instalado en `.venv`
- [x] `.zed/launch.json` configurado correctamente
- [x] `.zed/settings.json` corregido (sin errores JSON)
- [x] `.zed/tasks.json` con tasks de ejecución
- [x] Scripts de debug manuales (`.zed/debug_main.sh`)
- [x] Documentación completa en `.zed/`

### 🔄 Lo que necesitas hacer:

1. **Reiniciar Zed** para que cargue la configuración corregida
2. **Presionar F5** y verificar que aparezcan las opciones
3. Si no aparecen, usar el script manual

---

## 💡 Consejo Pro

**Workflow recomendado:**

1. Abre Zed
2. Abre `main.py` (o cualquier archivo)
3. Coloca breakpoints donde necesites
4. Presiona **F5**
5. Si aparece el menú → Selecciona `🚀 Debug Creative Flow`
6. Si NO aparece → Abre una terminal y ejecuta `.zed/debug_main.sh`

**Lo importante:** No importa qué método uses, lo que importa es que puedas debuggear tu código.

---

## 📚 Más Ayuda

Si sigues teniendo problemas, consulta estos archivos:

- **COMO_DEBUGGEAR_MAIN.md** - Guía detallada y completa
- **DEBUG_GUIDE.md** - Guía técnica de debugging
- **DEBUG_EXAMPLES.md** - Ejemplos prácticos específicos

O simplemente usa el script manual que siempre funciona:
```bash
.zed/debug_main.sh
```

---

## ✅ Checklist de Debug

Antes de pedir ayuda, verifica:

- [ ] He reiniciado Zed completamente
- [ ] Los archivos JSON no tienen errores (verificado con `python -m json.tool`)
- [ ] `debugpy` está instalado (`.venv/bin/pip list | grep debugpy`)
- [ ] He guardado todos los archivos (Ctrl+S)
- [ ] He probado el script manual `.zed/debug_main.sh`

---

_Última actualización: 27 de enero, 2025_

_Si nada funciona, abre una terminal y ejecuta `.zed/debug_main.sh` - ese método SIEMPRE funciona._