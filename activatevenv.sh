#!/bin/bash

# Setează numele folderului venv
VENV_DIR="venv"

# Creează venv dacă nu există
if [ ! -d "$VENV_DIR" ]; then
    echo "Creare mediu virtual în ./$VENV_DIR ..."
    python3 -m venv "$VENV_DIR"
fi

# Activează venv
echo "Activare mediu virtual..."
source "$VENV_DIR/bin/activate"

# Instalează pachetele din requirements.txt dacă există
if [ -f "requirements.txt" ]; then
    echo "Instalare pachete din requirements.txt ..."
    pip install -r requirements.txt
else
    echo "Fișier requirements.txt nu a fost găsit."
fi

# Confirmare
echo "Mediul virtual este activat. Promptul ar trebui să înceapă cu (venv)."
