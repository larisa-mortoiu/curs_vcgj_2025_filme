#!/bin/sh

echo "Activare venv:"
#source .vanv/bin/activate
. .venv/bin/activate

echo "Configurare variabila de mediu FLASK_APP"
export FLASK_APP=filme

echo "Pornire aplicație..."
python3 filme.py