FROM python:3.11-alpine

ENV FLASK_APP filme

# 1. Creezi utilizatorul
RUN adduser -D dina_docker

# 2. Setezi directorul de lucru
WORKDIR /home/dina_docker

# 3. Copiezi fișierele și setezi permisiuni
COPY app app
COPY templates templates
COPY static static
COPY dockerstart.sh dockerstart.sh
RUN chmod +x dockerstart.sh && chown dina_docker:dina_docker dockerstart.sh

COPY pytest.ini pytest.ini
COPY requirements.txt requirements.txt
COPY filme.py filme.py

# 4. Creezi venv și instalezi requirements
RUN python3 -m venv .venv
RUN .venv/bin/pip install -r requirements.txt

# 5. Treci la user non-root
USER dina_docker

# 6. Configurare finală
EXPOSE 5011
ENTRYPOINT ["sh", "./dockerstart.sh"]

