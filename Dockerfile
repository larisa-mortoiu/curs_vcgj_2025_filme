FROM python:3.10-alpine

# Creează utilizator non-root
RUN adduser -D movieuser

# Setează directorul de lucru
WORKDIR /home/movieuser/app

# Copiază fișierele aplicației în container
COPY filme.py .
COPY quickrequirements.txt .

# Creează și activează mediu virtual + instalează dependențele
RUN python3 -m venv .venv && \
    .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

# Rulează aplicația ca user non-root
USER movieuser

# Expune portul Flask
EXPOSE 5050

# Rulează aplicația Flask cu gunicorn
CMD [".venv/bin/gunicorn", "-b", "0.0.0.0:5050", "filme:app"]
