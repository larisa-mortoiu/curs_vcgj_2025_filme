#!/bin/bash
echo " Activare mediu virtual..."
. .venv/bin/activate

echo " Configurare variabilă de mediu FLASK_APP..."
export FLASK_APP=filme

echo " Pornire aplicație Flask..."
python3 filme.py
