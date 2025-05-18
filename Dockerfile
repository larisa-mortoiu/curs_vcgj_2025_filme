FROM python:3.10-slim

# Instalăm pachetele necesare pentru venv
RUN apt-get update && apt-get install -y \
    python3-venv \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Creăm un user neprivilegiat
RUN adduser --disabled-password --gecos "" filme

# Director de lucru
WORKDIR /home/filme/app

# Copiem fișierele aplicației
COPY . .

# Creăm mediu virtual și instalăm dependințele
RUN python3 -m venv .venv && \
    .venv/bin/pip install --upgrade pip && \
    .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

# Setăm utilizator non-root
USER filme

# Port aplicație
EXPOSE 5050
ENV PYTHONPATH="/home/filme/app:/home/filme"

# Pornire server Flask cu gunicorn
CMD [".venv/bin/gunicorn", "-b", "0.0.0.0:5050", "filme:app"]

