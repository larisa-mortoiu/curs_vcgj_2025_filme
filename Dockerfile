FROM python:3.10-slim

WORKDIR /app

COPY . .

# Instalează direct în mediul containerului (fără venv)
RUN pip install --upgrade pip && pip install flask pytest

EXPOSE 5000

CMD ["python", "filme.py"]

