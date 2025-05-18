#!/bin/bash

# Activează mediul virtual local
if [ ! -d "venv" ]; then
    echo "⚠️  Mediu virtual 'venv' nu există. Creează-l cu ./activeaza_venv.sh"
    exit 1
fi

echo "✅ Activare mediu virtual..."
source venv/bin/activate

# Rulează aplicația Flask
echo "🚀 Pornire aplicație Flask..."
python filme.py

