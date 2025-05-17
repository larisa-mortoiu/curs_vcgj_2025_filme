FROM python:3.10-alpine

# Creează utilizator non-root
RUN adduser -D movieuser

# Creează directorul aplicației și îl setează ca director de lucru
WORKDIR /home/movieuser/app

# Copiază fișierele aplicației
COPY app/ app/
COPY filme.py .
COPY quickrequirements.txt .

# Creează și activează mediul virtual + instalează dependințele
RUN python3 -m venv .venv && \
    .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

# Trecere la utilizator non-root
USER movieuser

# Expune portul folosit de Flask
EXPOSE 5050

# Rulează aplicația Flask cu Gunicorn
CMD [".venv/bin/gunicorn", "-b", "0.0.0.0:5050", "filme:app"]
