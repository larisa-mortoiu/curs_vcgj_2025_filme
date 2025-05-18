#!/bin/sh

# Activăm mediul virtual
. .venv/bin/activate

# Setăm variabilele de mediu pentru Flask
export FLASK_APP=filme.py
export FLASK_ENV=production  # sau development dacă vrei

# Pornim aplicația Flask
flask run --host=0.0.0.0 --port=5011

