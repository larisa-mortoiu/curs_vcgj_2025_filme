FROM python:3.10-alpine

# Creează un utilizator non-root numit 'filme'
RUN adduser -D filme

# Setează directorul de lucru
WORKDIR /home/filme/app

# Copiază fișierele aplicației
COPY filme.py .
COPY quickrequirements.txt quickrequirements.txt

# Creează un mediu virtual și instalează pachetele
RUN python3 -m venv .venv
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

# Rulează aplicația ca utilizator non-root
USER filme

# Expune portul pe care rulează aplicația
EXPOSE 5050

# Pornește aplicația cu gunicorn
CMD [".venv/bin/gunicorn", "-b", "0.0.0.0:5050", "filme:app"]

