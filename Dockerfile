# Imagine de bază oficială Python
FROM python:3.10-slim

# Setează directorul de lucru în container
WORKDIR /app

# Copiază fișierele aplicației în container
COPY . /app

# Instalează dependințele
RUN pip install --no-cache-dir flask

# Expune portul pe care rulează Flask
EXPOSE 5000

# Comanda de pornire a aplicației
CMD ["python3", "filme.py"]
