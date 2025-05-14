#!/bin/sh
echo "Activare venv:"
. .venv/bin/activate
#echo "Configurare variabila mediu FLASK_APP"
export FLASK_APP=filme
echo "Start server:"
exec flask run -h 0.0.0.0 -p 5011 --reload
