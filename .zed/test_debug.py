#!/usr/bin/env python3
"""
Script de prueba para verificar la configuración del debugger en Zed.

Este script prueba:
1. Importaciones básicas de Python
2. Importaciones de PySide6/Qt6
3. Puntos de breakpoint sugeridos
4. Inspección de variables

Uso:
    - Abre este archivo en Zed
    - Coloca breakpoints en las líneas marcadas con # <- BREAKPOINT
    - Presiona F5 para iniciar el debugger
    - Usa F10 para avanzar línea por línea
"""

import sys
import os

# <- BREAKPOINT 1: Coloca aquí un breakpoint para inspeccionar el entorno
print("=" * 60)
print("🔍 Test de Debugger para Creative Flow")
print("=" * 60)

# Test 1: Variables de entorno
print("\n📋 Test 1: Variables de Entorno")
qt_logging = os.environ.get("QT_LOGGING_RULES", "No configurado")
pythonpath = os.environ.get("PYTHONPATH", "No configurado")
qt_platform = os.environ.get("QT_QPA_PLATFORM", "No configurado")

# <- BREAKPOINT 2: Inspecciona las variables de entorno aquí
print(f"   QT_LOGGING_RULES: {qt_logging}")
print(f"   PYTHONPATH: {pythonpath}")
print(f"   QT_QPA_PLATFORM: {qt_platform}")

# Test 2: Importaciones de Qt6
print("\n📦 Test 2: Importaciones de PySide6")
try:
    from PySide6.QtCore import QCoreApplication, Qt, QTimer
    from PySide6.QtWidgets import QApplication, QPushButton
    print("   ✓ PySide6.QtCore importado correctamente")
    print("   ✓ PySide6.QtWidgets importado correctamente")
    qt_imported = True
except ImportError as e:
    print(f"   ✗ Error al importar PySide6: {e}")
    qt_imported = False

# Test 3: Variables complejas para inspección
print("\n🔢 Test 3: Tipos de Datos Complejos")

# <- BREAKPOINT 3: Inspecciona estas estructuras de datos
test_dict = {
    "nombre": "Creative Flow",
    "version": "1.0.0",
    "componentes": ["Qt6", "SQLite", "Python"],
    "configuracion": {
        "debug": True,
        "log_level": "INFO"
    }
}

test_list = [1, 2, 3, "cuatro", 5.0, {"seis": 6}]

test_tuple = ("Python", 3.11, True)

# <- BREAKPOINT 4: Verifica los valores antes de imprimirlos
print(f"   Dict: {test_dict}")
print(f"   List: {test_list}")
print(f"   Tuple: {test_tuple}")

# Test 4: Función con parámetros
def calcular_area(ancho, alto):
    """Función simple para probar step into/over."""
    # <- BREAKPOINT 5: Prueba F11 (step into) cuando llegues a esta función
    area = ancho * alto
    perimetro = 2 * (ancho + alto)
    return {
        "area": area,
        "perimetro": perimetro,
        "ancho": ancho,
        "alto": alto
    }

print("\n🧮 Test 4: Funciones")
rectangulo = calcular_area(10, 5)
# <- BREAKPOINT 6: Inspecciona el resultado de la función
print(f"   Rectángulo: {rectangulo}")

# Test 5: Loop para probar navegación
print("\n🔄 Test 5: Iteraciones")
contador = 0
for i in range(5):
    contador += i
    # <- BREAKPOINT 7: Coloca aquí para ver cómo cambian las variables en cada iteración
    print(f"   Iteración {i}: contador = {contador}")

# Test 6: Manejo de excepciones
print("\n⚠️  Test 6: Manejo de Excepciones")
try:
    # <- BREAKPOINT 8: Prueba step over (F10) vs step into (F11) aquí
    resultado = 10 / 2
    print(f"   División exitosa: {resultado}")

    # Esta línea causará una excepción si se descomenta
    # resultado_error = 10 / 0
except ZeroDivisionError as e:
    print(f"   ✗ Error capturado: {e}")
else:
    print("   ✓ No hubo errores")

# Test 7: Clase simple
class UsuarioTest:
    """Clase de prueba para debuggear objetos."""

    def __init__(self, nombre, edad):
        # <- BREAKPOINT 9: Inspecciona self durante la construcción
        self.nombre = nombre
        self.edad = edad
        self.activo = True

    def saludar(self):
        # <- BREAKPOINT 10: Inspecciona self en un método
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"

    def __repr__(self):
        return f"UsuarioTest(nombre='{self.nombre}', edad={self.edad})"

print("\n👤 Test 7: Objetos y Clases")
usuario = UsuarioTest("Juan", 30)
# <- BREAKPOINT 11: Inspecciona el objeto usuario
mensaje = usuario.saludar()
print(f"   {mensaje}")
print(f"   Usuario: {usuario}")

# Test 8: Qt Application (solo si Qt está disponible)
if qt_imported:
    print("\n🎨 Test 8: Aplicación Qt Mínima")

    # No creamos la aplicación completa para no bloquear el test
    # Pero verificamos que las clases estén disponibles
    print(f"   ✓ Qt Version: {Qt.DisplayRole}")
    print("   ✓ QApplication disponible")
    print("   ✓ QPushButton disponible")
    print("   (No se inicia QApplication para no bloquear el test)")

# Resumen final
print("\n" + "=" * 60)
print("✅ Test de Debugger Completado")
print("=" * 60)
print("\n💡 Próximos pasos:")
print("   1. Coloca breakpoints en las líneas marcadas")
print("   2. Presiona F5 para iniciar el debugger")
print("   3. Usa F10 (Step Over), F11 (Step Into), Shift+F11 (Step Out)")
print("   4. Inspecciona variables en el panel de debug")
print("   5. Cuando estés listo, prueba con main.py")
print("\n📖 Consulta .zed/DEBUG_GUIDE.md para más información\n")
