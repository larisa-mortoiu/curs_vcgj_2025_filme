# Imagine de bază
FROM python:3.10-slim

# Creează un director de lucru
WORKDIR /app

# Copiază fișierele necesare în imagine
COPY . .

# Instalează dependențele
RUN pip install --no-cache-dir -r quickrequirements.txt

# Expune portul aplicației
EXPOSE 5050

# Comandă pentru a porni aplicația
CMD ["gunicorn", "-b", "0.0.0.0:5050", "filme:app"]
