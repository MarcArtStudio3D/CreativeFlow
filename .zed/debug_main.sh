#!/bin/bash
# Script de launcher para debugging de Creative Flow
# Este script se ejecuta siempre desde el directorio raíz del proyecto

# Obtener el directorio del script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Cambiar al directorio del proyecto
cd "$PROJECT_DIR" || exit 1

# Variables de entorno para Qt6
export QT_LOGGING_RULES="qt.sql.qsqldatabase.warning=false"
export PYTHONPATH="$PROJECT_DIR"
export QT_QPA_PLATFORM="xcb"

# Python del entorno virtual
PYTHON_BIN="$PROJECT_DIR/.venv/bin/python"

# Verificar que el Python existe
if [ ! -f "$PYTHON_BIN" ]; then
    echo "❌ Error: No se encuentra Python en $PYTHON_BIN"
    echo "   Ejecuta: python -m venv .venv && .venv/bin/pip install -r requirements.txt"
    exit 1
fi

# Verificar que debugpy está instalado
if ! "$PYTHON_BIN" -c "import debugpy" 2>/dev/null; then
    echo "❌ Error: debugpy no está instalado"
    echo "   Ejecuta: .venv/bin/pip install debugpy"
    exit 1
fi

# Mostrar información
echo "🚀 Iniciando Creative Flow en modo debug..."
echo "   Proyecto: $PROJECT_DIR"
echo "   Python: $PYTHON_BIN"
echo "   Archivo: main.py"
echo ""

# Iniciar con debugpy
# Puerto 5678 es el puerto por defecto de debugpy
exec "$PYTHON_BIN" -m debugpy --listen 5678 --wait-for-client "$PROJECT_DIR/main.py"
