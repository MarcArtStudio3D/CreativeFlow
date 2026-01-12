# 🚀 Inicio Rápido - CreativeFlow

## Para Usuarios Nuevos (Primera Instalación)

### Linux / macOS
```bash
# 1. Clonar repositorio
git clone https://github.com/tu-usuario/CreativeFlow.git
cd CreativeFlow

# 2. Instalar automáticamente (TODO EN UNO)
./install.sh

# 3. Ejecutar
source .venv/bin/activate
python main.py
```

### Windows
```cmd
REM 1. Clonar repositorio
git clone https://github.com/tu-usuario/CreativeFlow.git
cd CreativeFlow

REM 2. Instalar automáticamente (TODO EN UNO)
install.bat

REM 3. Ejecutar
.venv\Scripts\activate.bat
python main.py
```

---

## Para Desarrolladores (Día a Día)

### Iniciar la aplicación
```bash
# Activar entorno virtual
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate.bat # Windows

# Ejecutar
python main.py
```

### Trabajar con interfaces Qt Designer

```bash
# 1. Editar archivo .ui con Qt Designer
qtdesigner ui/mi_pantalla.ui

# 2. Compilar todos los .ui a Python
./scripts/compile_ui.sh

# 3. Los archivos .py generados están en modulos/*/view/ui_*.py
# NO editar estos archivos directamente
```

### Verificar el entorno
```bash
# Verifica que todo esté configurado correctamente
./scripts/check_environment.sh
```

### Instalar nuevas dependencias
```bash
# 1. Activar entorno
source .venv/bin/activate

# 2. Instalar paquete
pip install nueva-libreria

# 3. Actualizar requirements.txt
pip freeze | grep nueva-libreria >> requirements.txt
```

---

## Comandos Útiles

### Ver estructura del proyecto
```bash
tree -L 2 -I '.venv|__pycache__|*.pyc'
```

### Limpiar archivos compilados
```bash
find . -type d -name '__pycache__' -exec rm -rf {} + 2>/dev/null
find . -name '*.pyc' -delete
```

### Verificar errores de importación
```bash
python -c "from login.controller import LoginController; print('✓ OK')"
```

### Ver logs de la aplicación
```bash
tail -f logs/app.log
```

---

## Estructura de Archivos Importantes

```
CreativeFlow/
├── main.py                    ← PUNTO DE ENTRADA
├── requirements.txt           ← Dependencias
├── install.sh / install.bat   ← Instaladores
├── styles.qss                 ← Estilos visuales
├── creativeflow.db            ← Base de datos SQLite
│
├── login/                     ← Módulo de login
│   ├── controller.py
│   ├── model.py
│   └── LoginScreen.py
│
├── modulos/                   ← Módulos de la app
│   ├── empresas/
│   ├── ventas/
│   ├── almacen/
│   └── ...
│
├── database/                  ← Gestión de BD
│   ├── database.py
│   └── CRUDempresas.py
│
├── scripts/                   ← Scripts de utilidad
│   ├── compile_ui.sh         ← Compilar interfaces
│   └── check_environment.sh  ← Verificar entorno
│
└── ui/                        ← Archivos Qt Designer (.ui)
    ├── designer.qrc
    ├── frmClientes.ui
    └── ...
```

---

## Problemas Comunes y Soluciones

### "Python no encontrado"
```bash
# Instalar Python 3.10+
# Ubuntu/Debian: sudo apt install python3
# macOS: brew install python3
# Windows: https://www.python.org/downloads/
```

### "Permission denied" en scripts
```bash
chmod +x install.sh
chmod +x scripts/*.sh
```

### "ModuleNotFoundError: No module named 'PySide6'"
```bash
# Activar entorno virtual primero
source .venv/bin/activate
pip install -r requirements.txt
```

### "No se ven bien los colores/estilos"
```bash
# Recompilar interfaces
./scripts/compile_ui.sh
```

### "Error de conexión a base de datos"
```bash
# Verificar que creativeflow.db existe
ls -lh creativeflow.db

# Si no existe, se creará al primer inicio
# Para MySQL/PostgreSQL: configurar desde panel admin
```

---

## Tips de Productividad

### Alias útiles (añadir a ~/.bashrc o ~/.zshrc)
```bash
alias cf='cd /ruta/a/CreativeFlow && source .venv/bin/activate'
alias cfrun='cf && python main.py'
alias cfui='cf && ./scripts/compile_ui.sh'
alias cfcheck='cf && ./scripts/check_environment.sh'
```

### Atajos de teclado (en la app)
- Ctrl+Q: Salir
- F5: Refrescar datos
- Ctrl+N: Nueva entrada
- Ctrl+S: Guardar

---

## Desarrollo de Nuevos Módulos

### Patrón MVC recomendado:

```
modulos/mi_modulo/
├── __init__.py
├── controller/
│   └── controller.py      # Lógica de negocio
├── model/
│   └── model.py           # Acceso a datos
└── view/
    ├── view.py            # Clase wrapper
    └── ui_mi_form.py      # Generado por compile_ui.sh
```

### Ejemplo controller.py:
```python
class MiModuloController:
    def __init__(self, view, model, session_data):
        self.view = view
        self.model = model
        self.session_data = session_data
        self.cargar_datos()
    
    def cargar_datos(self):
        datos = self.model.get_datos()
        # Actualizar vista...
```

---

## Recursos Adicionales

- **README.md**: Documentación completa
- **SETUP.md**: Guía técnica detallada
- **IMPORTAR_PANTALLAS.md**: Guía de interfaces
- **CHANGELOG.md**: Historial de versiones

---

## 🆘 Soporte

1. Ejecuta `./scripts/check_environment.sh`
2. Revisa logs en `logs/`
3. Consulta documentación en README.md
4. Abre issue en GitHub

---

**¡Listo! Ahora puedes desarrollar en CreativeFlow** 🚀

