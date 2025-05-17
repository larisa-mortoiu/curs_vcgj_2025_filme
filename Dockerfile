FROM python:3.10-alpine

# Creăm un user neprivilegiat numit `suits`
RUN adduser -D filme

# Setăm directorul de lucru
WORKDIR /home/filme/app

# Copiem fișierele aplicației
COPY filme.py .
COPY quickrequirements.txt .

# Creăm un mediu virtual și instalăm dependințele
RUN python3 -m venv .venv && \
    .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

# Rulăm aplicația ca utilizator non-root
USER filme

# Expunem portul Flask
EXPOSE 5050

# Pornim aplicația cu gunicorn
CMD [".venv/bin/gunicorn", "-b", "0.0.0.0:5050", "filme:app"]
