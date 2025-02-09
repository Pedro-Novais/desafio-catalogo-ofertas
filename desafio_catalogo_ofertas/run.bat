@echo off

set PROJECT_DIR=%~dp0

set VENV_DIR=%PROJECT_DIR%venv

if not exist "%VENV_DIR%" (
    echo Criando ambiente virtual...
    python -m venv "%VENV_DIR%"
)

echo Ativando ambiente virtual...
call "%VENV_DIR%\Scripts\activate.bat"

echo Instalando dependencias...
pip install -r "%PROJECT_DIR%requirements.txt"

echo Coletando dados dos produtos...
cd "%PROJECT_DIR%\scripts"
python web_scrapping.py

echo Iniciando o servidor Django...
cd "%PROJECT_DIR%"
python manage.py runserver

echo Processo concluído.
pause