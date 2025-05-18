#!/bin/bash

# Nume mediu virtual
VENV_NAME="venv"

# Creează mediul virtual dacă nu există
if [ ! -d "$VENV_NAME" ]; then
    echo "Se creează mediul virtual..."
    python3 -m venv $VENV_NAME
fi

# Activează mediul virtual
source $VENV_NAME/bin/activate
echo "Mediul virtual '$VENV_NAME' este activat."

# Instalează pachetele
pip install -r requirements.txt

