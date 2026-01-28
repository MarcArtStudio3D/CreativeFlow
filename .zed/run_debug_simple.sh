#!/bin/bash
# Script simple para debuggear Creative Flow
# NO usa --wait-for-client, inicia directamente

cd /home/marc/Artstudio3D/CreativeFlow || exit 1

export QT_LOGGING_RULES="qt.sql.qsqldatabase.warning=false"
export PYTHONPATH="/home/marc/Artstudio3D/CreativeFlow"
export QT_QPA_PLATFORM="xcb"

echo "🚀 Iniciando Creative Flow en modo debug..."
echo "📍 Coloca breakpoints en Zed antes de iniciar"
echo "🔌 Debugger escuchando en puerto 5678"
echo ""
echo "Para conectar desde Zed:"
echo "  1. Debug → Attach to Process"
echo "  2. localhost:5678"
echo ""
read -p "Presiona Enter cuando estés listo..."

# Inicia con debugpy pero SIN wait-for-client
exec .venv/bin/python -m debugpy --listen 0.0.0.0:5678 main.py
