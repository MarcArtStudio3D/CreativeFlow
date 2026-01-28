# 🔧 Solución al Problema de Timeout en Zed Debugger

## ❌ El Problema

Al intentar iniciar el debugger con F5, obtienes este error:

```
Tried to launch debugger with: {
  "request": "launch",
  "python": "${workspaceFolder}/.venv/bin/python",
  "args": [
    "--listen",
    "5678",
    "--wait-for-client",
    "${workspaceFolder}/main.py"
  ],
  "cwd": "${workspaceFolder}",
  "module": "debugpy",
  "console": "integratedTerminal"
}
error: Timed out waiting for launcher to connect
```

**Causa**: El debugger está usando `--wait-for-client` que hace que espere indefinidamente una conexión que nunca llega.

---

## ✅ Solución Implementada

He simplificado las configuraciones eliminando el modo "wait-for-client" y usando rutas relativas simples.

### Archivos Actualizados:

1. **`.zed/debug.json`** - Configuración simplificada sin wait-for-client
2. **`.zed/launch.json`** - Configuración VSCode-compatible simplificada
3. **`.zed/settings.json`** - Configuración del adaptador debugpy
4. **`.zed/tasks.json`** - Tareas sin opciones de debug problemáticas

---

## 🚀 Cómo Usar Ahora

### Método 1: Usando F5 (Recomendado)

1. **Abre cualquier archivo** de tu proyecto
2. **Coloca breakpoints** (clic en margen izquierdo o F9)
3. **Presiona F5**
4. **Selecciona**: `🚀 Debug Creative Flow`
5. **La aplicación debería iniciar** correctamente

### Método 2: Desde el Command Palette

1. **Ctrl+Shift+P** (abrir paleta de comandos)
2. **Escribe**: "debug"
3. **Selecciona**: "Debug: Start"
4. **Elige**: `🚀 Debug Creative Flow`

### Método 3: Manual (Si todo lo demás falla)

Si Zed sigue dando problemas, usa este método manual:

```bash
cd /home/marc/Artstudio3D/CreativeFlow

# Método A: Ejecutar sin debugger (para probar que funciona)
.venv/bin/python main.py

# Método B: Con debugpy en modo attach (requiere 2 terminales)
# Terminal 1:
.venv/bin/python -m debugpy --listen 5678 main.py

# Terminal 2 (en Zed, conectar al debugger):
# Debug → Attach → localhost:5678
```

---

## 🔍 Verificación

### 1. Verifica que los archivos JSON sean válidos:

```bash
cd /home/marc/Artstudio3D/CreativeFlow

python3 -m json.tool .zed/debug.json > /dev/null && echo "✓ debug.json OK"
python3 -m json.tool .zed/launch.json > /dev/null && echo "✓ launch.json OK"
python3 -m json.tool .zed/settings.json > /dev/null && echo "✓ settings.json OK"
python3 -m json.tool .zed/tasks.json > /dev/null && echo "✓ tasks.json OK"
```

Todos deberían mostrar "✓ ... OK"

### 2. Verifica que debugpy funciona:

```bash
.venv/bin/python -m debugpy --version
```

Debería mostrar: `1.8.19` (o superior)

### 3. Verifica que la app funciona sin debug:

```bash
.venv/bin/python main.py
```

La aplicación debería abrirse normalmente.

---

## 🐛 Si Aún No Funciona

### Opción A: Reiniciar Zed

A veces Zed necesita reiniciarse para recargar las configuraciones:

1. Cierra Zed completamente
2. Abre Zed de nuevo
3. Abre el proyecto Creative Flow
4. Intenta F5 de nuevo

### Opción B: Limpiar caché de Zed

```bash
# Cerrar Zed primero, luego:
rm -rf ~/.config/zed/.zed/
```

Luego abre Zed de nuevo y prueba.

### Opción C: Usar VSCode (temporal)

Si necesitas debuggear urgentemente mientras solucionamos el problema de Zed:

1. Abre el proyecto en VSCode:
   ```bash
   code /home/marc/Artstudio3D/CreativeFlow
   ```

2. VSCode debería reconocer automáticamente el `.zed/launch.json`

3. Presiona F5 en VSCode

### Opción D: Debugging con prints (old school pero funciona)

Agrega prints estratégicos en tu código:

```python
# En lugar de breakpoints, usa:
print(f"🔍 DEBUG: variable = {variable}")
print(f"🔍 DEBUG: llegó aquí - línea 123")

# Para objetos complejos:
import pprint
pprint.pprint(objeto)

# Para ver el stack trace:
import traceback
traceback.print_stack()
```

---

## 📋 Configuración Actual Simplificada

### debug.json

```json
[
  {
    "label": "🚀 Debug Creative Flow",
    "adapter": "debugpy",
    "type": "python",
    "request": "launch",
    "program": "main.py",
    "args": [],
    "env": {
      "QT_LOGGING_RULES": "qt.sql.qsqldatabase.warning=false",
      "PYTHONPATH": ".",
      "QT_QPA_PLATFORM": "xcb"
    }
  }
]
```

**Cambios clave**:
- ✅ Sin `--wait-for-client`
- ✅ Sin `--listen`
- ✅ Ruta simple `main.py` en lugar de `${workspaceFolder}/main.py`
- ✅ Solo las opciones esenciales

---

## 💡 Alternativa: Script de Debug Manual

He creado un script que puedes usar mientras solucionamos el problema de Zed:

```bash
# Ejecutar:
.zed/debug_main.sh
```

Este script:
1. Verifica que todo esté instalado
2. Configura las variables de entorno
3. Inicia debugpy correctamente
4. Espera en el puerto 5678 para que te conectes desde Zed

**Cómo usarlo con Zed:**
1. Ejecuta el script en una terminal: `.zed/debug_main.sh`
2. En Zed: Debug → Attach to Process → localhost:5678
3. Coloca breakpoints y empieza a debuggear

---

## 🎯 Workaround Definitivo (Si Zed no coopera)

Si después de todo esto Zed sigue sin funcionar, aquí hay un workaround garantizado:

### 1. Instala ipdb (debugger interactivo en terminal)

```bash
.venv/bin/pip install ipdb
```

### 2. En tu código, donde quieras debuggear, agrega:

```python
import ipdb; ipdb.set_trace()
```

### 3. Ejecuta la app normalmente:

```bash
.venv/bin/python main.py
```

### 4. Cuando llegue a esa línea:

- Se detendrá en la terminal
- Tendrás un prompt interactivo
- Puedes inspeccionar variables
- Comandos útiles:
  - `n` - siguiente línea (step over)
  - `s` - step into
  - `c` - continuar
  - `p variable` - imprimir variable
  - `pp variable` - pretty print
  - `l` - listar código
  - `h` - ayuda

---

## 🔄 Próximos Pasos

1. **Intenta F5** con la configuración simplificada
2. **Si funciona**: ¡Perfecto! Puedes debuggear normalmente
3. **Si no funciona**: 
   - Prueba el método manual (Terminal 1 + Attach)
   - O usa el workaround con ipdb
   - Mientras tanto, investigo más a fondo el problema de Zed

---

## 📞 Reportar el Problema

Si el problema persiste, podemos:

1. **Verificar versión de Zed**:
   ```bash
   zed --version
   ```

2. **Ver logs de Zed**:
   En Zed: Help → View Logs
   Busca errores relacionados con "debugpy" o "python"

3. **Verificar permisos**:
   ```bash
   ls -la .zed/
   # Todos los archivos deben ser legibles
   ```

---

## ✅ Checklist de Troubleshooting

- [ ] Todos los JSON son válidos (sin errores de sintaxis)
- [ ] debugpy está instalado (`.venv/bin/pip list | grep debugpy`)
- [ ] La app funciona sin debug (`.venv/bin/python main.py`)
- [ ] He reiniciado Zed después de cambiar las configuraciones
- [ ] No hay otros procesos de Python colgados (ps aux | grep python)
- [ ] El puerto 5678 no está ocupado (`lsof -i :5678`)

---

## 📚 Documentación de Referencia

- **Zed Debugger**: https://zed.dev/docs/debugging
- **debugpy**: https://github.com/microsoft/debugpy
- **ipdb**: https://github.com/gotcha/ipdb

---

_Última actualización: 27 de enero, 2025_  
_Si encuentras la solución, por favor documéntala aquí para futuras referencias_