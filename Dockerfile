# Folosește o imagine oficială Python
FROM python:3.10-slim

# Setează directorul de lucru în container
WORKDIR /app

# Copiază tot codul în container
COPY . .

# Instalează dependințele
RUN python -m venv venv \
    && . venv/bin/activate \
    && pip install --upgrade pip \
    && pip install flask pytest

# Expune portul Flask (default 5000)
EXPOSE 5000

# Rulează aplicația
CMD ["venv/bin/python", "filme.py"]

