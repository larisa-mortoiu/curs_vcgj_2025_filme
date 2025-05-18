#!/bin/bash

# Numele directorului pentru mediul virtual
VENV_DIR="venv"

# Funcție pentru afișarea erorilor și oprirea execuției
function exit_with_error() {
    echo "Eroare: $1"
    exit 1
}

# Verifică dacă python3 este disponibil
command -v python3 >/dev/null 2>&1 || exit_with_error "Python3 nu este instalat sau nu este în PATH."

# Creează mediul virtual dacă nu există deja
if [ ! -d "$VENV_DIR" ]; then
    echo "Creare mediu virtual în ./$VENV_DIR ..."
    python3 -m venv "$VENV_DIR" || exit_with_error "Crearea mediului virtual a eșuat."
else
    echo "Mediul virtual deja există în ./$VENV_DIR"
fi

# Activează mediul virtual
if [ -f "$VENV_DIR/bin/activate" ]; then
    echo "Activare mediu virtual..."
    source "$VENV_DIR/bin/activate"
else
    exit_with_error "Scriptul de activare nu a fost găsit în $VENV_DIR/bin/activate."
fi

# Instalează pachetele dacă există fișierul requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Instalare pachete din requirements.txt ..."
    pip install -r requirements.txt || exit_with_error "Instalarea pachetelor a eșuat."
else
    echo "Atenție: Fișierul requirements.txt nu a fost găsit."
fi

# Confirmare finală
echo "✅ Mediul virtual este activat cu succes."
echo "💡 Promptul ar trebui să înceapă cu (venv)."