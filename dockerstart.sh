#!/bin/sh
echo "Activare venv:"
. ./activeaza_venv
echo "Configurare variabila mediu FLASK_APP"
export FLASK_APP=filme
echo "Start server:"
exec flask run -h 0.0.0.0 -p 25568 --reload
