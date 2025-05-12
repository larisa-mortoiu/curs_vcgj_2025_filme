#!/bin/bash

# Încearcă să activezi venv-ul
. .venv/bin/activate

# Dacă nu există, îl creează și instalează requirements
if [ $? -eq 0 ]; then
    echo "SUCCESS: venv was activated."
else
    echo "FAIL: .venv not found. Creating one..."
    python3 -m venv .venv
    source .venv/bin/activate

    echo "Installing requirements..."
    pip install --upgrade pip
    pip install -r requirements.txt

    echo "venv created and requirements installed."
fi
