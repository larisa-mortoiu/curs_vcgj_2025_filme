# Imagine de bază cu Python 3.10
FROM python:3.10-slim

# Setează directorul de lucru
WORKDIR /app

# Copiază toate fișierele în container
COPY . .

# Instalează dependențele
RUN pip install --no-cache-dir -r requirements.txt

# Expune portul pe care Flask rulează implicit
EXPOSE 5000

# Rulează aplicația
CMD ["python", "filme.py"]

