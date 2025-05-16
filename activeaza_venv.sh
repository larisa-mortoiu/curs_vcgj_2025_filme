#!/bin/bash

# Activează sau creează venv
if [ -d ".venv" ]; then
    echo "Activating existing venv..."
    . .venv/bin/activate
else
    echo "Creating new virtual environment..."
    python3 -m venv .venv
    . .venv/bin/activate
fi

# Instalează/actualizează pachetele
echo "Installing/Updating requirements..."
pip install --upgrade pip
pip install -r requirements.txt

