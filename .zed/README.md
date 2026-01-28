# Configuración de Zed para Creative Flow

## 📁 Archivos de Configuración

Este directorio contiene la configuración personalizada de Zed para el proyecto Creative Flow.

### Archivos Principales

- **`debug.json`** - Configuración del debugger para Python con Qt6
- **`settings.json`** - Configuración del editor, LSP, atajos de teclado y tareas
- **`launch.json`** - Configuración alternativa de lanzamiento (VSCode compatible)
- **`DEBUG_GUIDE.md`** - Guía completa de uso del debugger
- **`test_debug.py`** - Script de prueba para verificar la configuración
- **`README.md`** - Este archivo

## 🚀 Inicio Rápido

### 1. Verificar Instalación

Asegúrate de que `debugpy` está instalado en tu entorno virtual:

```bash
.venv/bin/pip list | grep debugpy
```

Si no está instalado:

```bash
.venv/bin/pip install debugpy
```

### 2. Probar Configuración

Ejecuta el script de prueba:

```bash
.venv/bin/python .zed/test_debug.py
```

### 3. Iniciar Debug de la Aplicación

1. Abre `main.py` en Zed
2. Coloca un breakpoint (clic en el margen izquierdo o presiona `F9`)
3. Presiona `F5` para iniciar el debugger
4. La aplicación se ejecutará y se detendrá en tu breakpoint

## ⌨️ Atajos de Teclado

| Tecla | Acción |
|-------|--------|
| `F5` | Iniciar/Continuar Debug |
| `F9` | Toggle Breakpoint |
| `F10` | Step Over (siguiente línea) |
| `F11` | Step Into (entrar en función) |
| `Shift+F11` | Step Out (salir de función) |
| `Shift+F5` | Detener Debug |

## 🔧 Configuración Actual

### Debugger

- **Tipo**: Python con debugpy
- **Archivo principal**: `main.py`
- **Python**: `/home/marc/Artstudio3D/CreativeFlow/.venv/bin/python`
- **Consola**: Terminal integrado

### Variables de Entorno

```json
{
  "QT_LOGGING_RULES": "qt.sql.qsqldatabase.warning=false",
  "PYTHONPATH": "${workspaceFolder}",
  "QT_QPA_PLATFORM": "xcb"
}
```

### Opciones de Debug

- **justMyCode**: `false` - Permite debuggear también código de librerías
- **stopOnEntry**: `false` - No se pausa al inicio automáticamente

## 📚 Documentación Completa

Para una guía detallada sobre cómo usar el debugger, consulta:

👉 **[DEBUG_GUIDE.md](DEBUG_GUIDE.md)**

Incluye:
- Instrucciones paso a paso
- Lugares comunes para breakpoints
- Tips y trucos
- Solución de problemas
- Ejemplos de sesiones de debug

## 🎯 Características Especiales

### 1. Debug de Qt6

La configuración está optimizada para aplicaciones Qt6:
- Variables de entorno preconfiguradas
- Soporte para widgets y señales/slots
- Terminal integrado para ver logs de Qt

### 2. LSP de Python

Pyright está configurado con:
- Type checking básico
- Auto-búsqueda de paths
- Integración con el venv del proyecto

### 3. Formateo de Código

Black está configurado como formateador externo usando el instalado en `.venv`

### 4. Tareas Personalizadas

Dos tareas disponibles en la paleta de comandos:

- **debug_python**: Ejecuta `python main.py`
- **run_app**: Ejecuta la aplicación con el entorno configurado

## 🐛 Solución de Problemas

### El debugger no inicia

1. Verifica que debugpy esté instalado
2. Comprueba que la ruta del Python sea correcta
3. Revisa que `debug.json` tenga JSON válido

### Los breakpoints no funcionan

1. Guarda el archivo antes de debuggear
2. Asegúrate de que el breakpoint esté en una línea ejecutable
3. Verifica que el archivo esté en el PYTHONPATH

### La ventana Qt no aparece

1. Verifica `QT_QPA_PLATFORM` (puede necesitar `wayland` en lugar de `xcb`)
2. Comprueba que PySide6 esté instalado correctamente
3. Revisa los logs en la consola integrada

## 📞 Soporte

Si encuentras problemas:

1. Consulta `DEBUG_GUIDE.md` para soluciones comunes
2. Revisa los logs en la terminal integrada de Zed
3. Ejecuta `test_debug.py` para verificar la configuración base

## 🔄 Actualización de Configuración

Para modificar la configuración de debug, edita `debug.json`:

```json
{
  "label": "Debug Creative Flow",
  "adapter": "debugpy",
  "program": "main.py",
  "pythonPath": "/ruta/al/python",
  "args": [],
  "env": {
    "VARIABLE": "valor"
  }
}
```

## ✅ Checklist de Verificación

- [ ] debugpy instalado en `.venv`
- [ ] `debug.json` con JSON válido
- [ ] Python path correcto en la configuración
- [ ] PySide6 instalado y funcionando
- [ ] `test_debug.py` ejecuta sin errores
- [ ] Breakpoints funcionan correctamente
- [ ] Variables se inspeccionan correctamente
- [ ] La aplicación Qt se muestra durante debug

---

**Última actualización**: 27 de enero, 2025  
**Versión de configuración**: 1.0  
**Compatible con**: Zed Editor, Python 3.11+, PySide6/Qt6