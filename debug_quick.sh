#!/bin/bash
# Script rápido para probar debug SIN necesitar configurar nada en Zed

echo "🚀 Iniciando Creative Flow con Debug..."
echo ""
echo "📌 INSTRUCCIONES:"
echo "   1. La aplicación se ejecutará en modo debug"
echo "   2. Puedes ver los logs en esta terminal"
echo "   3. Para debug avanzado, usa Zed después de reiniciarlo"
echo ""
echo "▶️  Iniciando en 2 segundos..."
sleep 2

cd /home/marc/Artstudio3D/CreativeFlow
source .venv/bin/activate

export QT_LOGGING_RULES="qt.sql.qsqldatabase.warning=false"
export PYTHONPATH="/home/marc/Artstudio3D/CreativeFlow"
export QT_QPA_PLATFORM="xcb"

python main.py
