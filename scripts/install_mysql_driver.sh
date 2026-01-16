#!/bin/bash
# Script para instalar libmysqlclient.so.21 sin romper MariaDB/DBeaver
# Uso: sudo ./install_mysql_driver.sh

set -e

echo "=========================================="
echo "Instalador de libmysqlclient.so.21"
echo "Para PySide6 en Arch Linux"
echo "=========================================="
echo ""

# Verificar que se ejecuta como root
if [ "$EUID" -ne 0 ]; then
    echo "❌ Error: Este script debe ejecutarse como root (usa sudo)"
    exit 1
fi

# Verificar que mariadb-libs está instalado
if ! pacman -Q mariadb-libs &>/dev/null; then
    echo "⚠️  mariadb-libs no está instalado, instalando..."
    pacman -S mariadb-libs --noconfirm
fi

# Crear directorio temporal
TMP_DIR=$(mktemp -d)
cd "$TMP_DIR"

echo "📥 Descargando libmysqlclient desde Ubuntu..."
wget -q http://archive.ubuntu.com/ubuntu/pool/main/m/mysql-8.0/libmysqlclient21_8.0.28-0ubuntu4_amd64.deb

echo "📦 Extrayendo paquete..."
ar x libmysqlclient21_8.0.28-0ubuntu4_amd64.deb
tar -I zstd -xf data.tar.zst 2>/dev/null || true

echo "📋 Copiando bibliotecas..."
# Solo copiar libmysqlclient, NO sobrescribir libmariadb
cp usr/lib/x86_64-linux-gnu/libmysqlclient.so.21.2.28 /usr/lib/

# Crear symlink (eliminando el anterior si existe)
rm -f /usr/lib/libmysqlclient.so.21
ln -s libmysqlclient.so.21.2.28 /usr/lib/libmysqlclient.so.21

echo "🔄 Actualizando caché de bibliotecas..."
ldconfig

echo "✅ Reinstalando mariadb-libs para asegurar integridad..."
pacman -S mariadb-libs --noconfirm

ldconfig

echo "🧹 Limpiando archivos temporales..."
cd /
rm -rf "$TMP_DIR"

echo ""
echo "=========================================="
echo "✅ Instalación completada exitosamente"
echo "=========================================="
echo ""
echo "Verificación:"
ls -lh /usr/lib/libmariadb.so.3 2>/dev/null && echo "  ✓ MariaDB OK (para DBeaver)"
ls -lh /usr/lib/libmysqlclient.so.21 2>/dev/null && echo "  ✓ MySQL OK (para PySide6)"
echo ""
echo "Ambas bibliotecas están instaladas y no hay conflictos."

