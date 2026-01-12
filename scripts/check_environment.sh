#!/usr/bin/env bash
# Script de verificación del entorno CreativeFlow
# Verifica que todas las dependencias y configuraciones estén correctas

echo "🔍 CreativeFlow - Verificación de Entorno"
echo "=========================================="
echo ""

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Función para mostrar OK
ok() {
    echo -e "${GREEN}✓${NC} $1"
}

# Función para mostrar ERROR
error() {
    echo -e "${RED}✗${NC} $1"
}

# Función para mostrar WARNING
warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Verificar Python
echo "1. Verificando Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
    MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

    if [ "$MAJOR" -eq 3 ] && [ "$MINOR" -ge 10 ]; then
        ok "Python $(python3 --version 2>&1) encontrado"
    else
        error "Python $PYTHON_VERSION encontrado, pero se requiere 3.10+"
        exit 1
    fi
else
    error "Python3 no encontrado"
    exit 1
fi
echo ""

# Verificar entorno virtual
echo "2. Verificando entorno virtual..."
if [ -d ".venv" ]; then
    ok "Entorno virtual encontrado (.venv)"

    # Verificar si está activado
    if [[ "$VIRTUAL_ENV" != "" ]]; then
        ok "Entorno virtual activado: $VIRTUAL_ENV"
    else
        warning "Entorno virtual no activado. Ejecuta: source .venv/bin/activate"
    fi
else
    error "Entorno virtual no encontrado (.venv)"
    echo "   Ejecuta: python3 -m venv .venv"
    exit 1
fi
echo ""

# Verificar dependencias
echo "3. Verificando dependencias instaladas..."
source .venv/bin/activate 2>/dev/null || true

# Lista de dependencias con nombres de módulos correctos
declare -A dependencies=(
    ["PySide6"]="PySide6"
    ["mysql-connector-python"]="mysql.connector"
    ["psycopg2"]="psycopg2"
    ["bcrypt"]="bcrypt"
)
all_ok=true

for dep_name in "${!dependencies[@]}"; do
    module_name="${dependencies[$dep_name]}"
    if python3 -c "import ${module_name}" 2>/dev/null; then
        VERSION=$(python3 -c "import ${module_name}; print(${module_name}.__version__ if hasattr(${module_name}, '__version__') else 'installed')" 2>/dev/null || echo "installed")
        ok "$dep_name ($VERSION)"
    else
        error "$dep_name no instalado"
        all_ok=false
    fi
done

if [ "$all_ok" = false ]; then
    echo ""
    warning "Algunas dependencias faltan. Ejecuta: pip install -r requirements.txt"
fi
echo ""

# Verificar archivos principales
echo "4. Verificando archivos del proyecto..."
files=("main.py" "MainWindow.py" "config.py" "styles.qss" "requirements.txt")

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        ok "$file existe"
    else
        error "$file no encontrado"
    fi
done
echo ""

# Verificar base de datos
echo "5. Verificando base de datos..."
if [ -f "creativeflow.db" ]; then
    SIZE=$(du -h creativeflow.db | cut -f1)
    ok "Base de datos SQLite encontrada (tamaño: $SIZE)"
else
    warning "Base de datos no encontrada (se creará al primer uso)"
fi
echo ""

# Verificar módulos compilados
echo "6. Verificando archivos compilados..."
if [ -f "modulos/designer_rc.py" ]; then
    ok "Recursos Qt compilados (designer_rc.py)"
else
    error "Recursos Qt no compilados"
    echo "   Ejecuta: ./scripts/compile_ui.sh"
fi

# Contar archivos UI compilados
UI_COUNT=$(find modulos -name "ui_*.py" 2>/dev/null | wc -l)
if [ "$UI_COUNT" -gt 0 ]; then
    ok "Archivos UI compilados: $UI_COUNT"
else
    warning "No se encontraron archivos UI compilados"
    echo "   Ejecuta: ./scripts/compile_ui.sh"
fi
echo ""

# Verificar estructura de carpetas
echo "7. Verificando estructura de carpetas..."
folders=("database" "login" "modulos" "scripts" "ui" "helpers")

for folder in "${folders[@]}"; do
    if [ -d "$folder" ]; then
        ok "$folder/"
    else
        error "$folder/ no encontrado"
    fi
done
echo ""

# Verificar permisos de scripts
echo "8. Verificando permisos de scripts..."
if [ -x "scripts/compile_ui.sh" ]; then
    ok "scripts/compile_ui.sh ejecutable"
else
    warning "scripts/compile_ui.sh no ejecutable"
    echo "   Ejecuta: chmod +x scripts/compile_ui.sh"
fi

if [ -x "install.sh" ]; then
    ok "install.sh ejecutable"
else
    warning "install.sh no ejecutable"
    echo "   Ejecuta: chmod +x install.sh"
fi
echo ""

# Test de importación
echo "9. Probando importaciones principales..."
if python3 -c "from PySide6.QtWidgets import QApplication" 2>/dev/null; then
    ok "PySide6.QtWidgets importable"
else
    error "Error importando PySide6.QtWidgets"
fi

if python3 -c "from login.controller import LoginController" 2>/dev/null; then
    ok "LoginController importable"
else
    error "Error importando LoginController"
fi

if python3 -c "from database.database import DataManager" 2>/dev/null; then
    ok "DataManager importable"
else
    error "Error importando DataManager"
fi
echo ""

# Resumen
echo "=========================================="
echo "📊 Resumen de verificación"
echo "=========================================="
echo ""
echo "Para iniciar la aplicación:"
echo "  1. source .venv/bin/activate"
echo "  2. python main.py"
echo ""
echo "Para compilar interfaces:"
echo "  ./scripts/compile_ui.sh"
echo ""
echo "Para instalar dependencias faltantes:"
echo "  pip install -r requirements.txt"
echo ""

