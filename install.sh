#!/usr/bin/env bash
# Script de instalación para CreativeFlow
# Compatible con Linux y macOS

set -e

echo "🚀 Instalando CreativeFlow - Project Pipeline Management"
echo "=========================================================="
echo ""

# Detectar Python
PYTHON_CMD=""
for cmd in python3.12 python3.11 python3.10 python3 python; do
    if command -v $cmd &> /dev/null; then
        VERSION=$($cmd --version 2>&1 | grep -oP '(?<=Python )\d+\.\d+')
        MAJOR=$(echo $VERSION | cut -d. -f1)
        MINOR=$(echo $VERSION | cut -d. -f2)

        if [ "$MAJOR" -eq 3 ] && [ "$MINOR" -ge 10 ]; then
            PYTHON_CMD=$cmd
            echo "✓ Python encontrado: $cmd (versión $VERSION)"
            break
        fi
    fi
done

if [ -z "$PYTHON_CMD" ]; then
    echo "❌ Error: Se requiere Python 3.10 o superior"
    echo "   Instala Python desde: https://www.python.org/downloads/"
    exit 1
fi

# Crear entorno virtual
echo ""
echo "📦 Creando entorno virtual..."
if [ -d ".venv" ]; then
    echo "   ⚠ Ya existe un entorno virtual (.venv)"
    read -p "   ¿Deseas recrearlo? (s/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        rm -rf .venv
        $PYTHON_CMD -m venv .venv
        echo "   ✓ Entorno virtual recreado"
    else
        echo "   ℹ Usando entorno virtual existente"
    fi
else
    $PYTHON_CMD -m venv .venv
    echo "   ✓ Entorno virtual creado"
fi

# Activar entorno virtual
source .venv/bin/activate

# Actualizar pip
echo ""
echo "🔧 Actualizando pip..."
pip install --upgrade pip setuptools wheel

# Instalar dependencias
echo ""
echo "📚 Instalando dependencias..."
pip install -r requirements.txt

# Dar permisos a scripts
echo ""
echo "🔐 Configurando permisos de scripts..."
chmod +x scripts/*.sh 2>/dev/null || true
chmod +x scripts/compile_ui.sh
echo "   ✓ Permisos configurados"

# Compilar archivos UI
echo ""
echo "🎨 Compilando archivos de interfaz..."
if [ -f "scripts/compile_ui.sh" ]; then
    ./scripts/compile_ui.sh
    echo "   ✓ Interfaces compiladas"
else
    echo "   ⚠ Script de compilación no encontrado"
fi

# Verificar base de datos
echo ""
echo "🗄️  Verificando base de datos..."
if [ -f "creativeflow.db" ]; then
    echo "   ✓ Base de datos encontrada"
else
    echo "   ⚠ Base de datos no encontrada"
    echo "   ℹ Se creará automáticamente al primer uso"
fi

# Resumen
echo ""
echo "=========================================================="
echo "✅ Instalación completada"
echo ""
echo "Para iniciar la aplicación:"
echo "  1. Activa el entorno virtual:"
echo "     source .venv/bin/activate"
echo ""
echo "  2. Ejecuta la aplicación:"
echo "     python main.py"
echo ""
echo "Para desarrollo:"
echo "  - Compilar UIs: ./scripts/compile_ui.sh"
echo "  - Ver errores: cat logs/app.log"
echo ""
echo "Documentación en README.md"
echo "=========================================================="

