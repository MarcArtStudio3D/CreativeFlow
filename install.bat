@echo off
REM Script de instalación para CreativeFlow en Windows
REM Requiere Python 3.10 o superior

echo ================================================
echo CreativeFlow - Project Pipeline Management
echo Script de Instalacion para Windows
echo ================================================
echo.

REM Verificar Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no encontrado en PATH
    echo Por favor instala Python 3.10+ desde: https://www.python.org/downloads/
    echo Asegurate de marcar "Add Python to PATH" durante la instalacion
    pause
    exit /b 1
)

REM Verificar versión de Python
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [OK] Python encontrado: %PYTHON_VERSION%
echo.

REM Crear entorno virtual
echo [PASO 1] Creando entorno virtual...
if exist .venv (
    echo Ya existe un entorno virtual
    set /p RECREATE="Deseas recrearlo? (S/N): "
    if /i "%RECREATE%"=="S" (
        echo Eliminando entorno virtual anterior...
        rmdir /s /q .venv
        python -m venv .venv
        echo [OK] Entorno virtual recreado
    ) else (
        echo [OK] Usando entorno virtual existente
    )
) else (
    python -m venv .venv
    echo [OK] Entorno virtual creado
)
echo.

REM Activar entorno virtual
echo [PASO 2] Activando entorno virtual...
call .venv\Scripts\activate.bat
echo [OK] Entorno virtual activado
echo.

REM Actualizar pip
echo [PASO 3] Actualizando pip...
python -m pip install --upgrade pip setuptools wheel
echo [OK] pip actualizado
echo.

REM Instalar dependencias
echo [PASO 4] Instalando dependencias...
pip install -r requirements.txt
echo [OK] Dependencias instaladas
echo.

REM Compilar archivos UI
echo [PASO 5] Compilando interfaces de usuario...
if exist scripts\compile_ui.sh (
    echo Ejecutando desde Git Bash o WSL recomendado
    echo O compila manualmente con: pyside6-uic
) else (
    echo [ADVERTENCIA] Script de compilacion no encontrado
)
echo.

REM Verificar base de datos
echo [PASO 6] Verificando base de datos...
if exist creativeflow.db (
    echo [OK] Base de datos encontrada
) else (
    echo [ADVERTENCIA] Base de datos no encontrada
    echo Se creara automaticamente al primer uso
)
echo.

REM Resumen
echo ================================================
echo Instalacion completada
echo ================================================
echo.
echo Para iniciar la aplicacion:
echo   1. Activa el entorno virtual:
echo      .venv\Scripts\activate.bat
echo.
echo   2. Ejecuta la aplicacion:
echo      python main.py
echo.
echo Para desarrollo:
echo   - Ver logs: type logs\app.log
echo   - Compilar UIs: Usar Git Bash o WSL
echo.
echo Documentacion en README.md
echo ================================================
pause

