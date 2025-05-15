FROM python:3.11-alpine

RUN apk add --no-cache python3-dev py3-pip py3-virtualenv gcc musl-dev

ENV FLASK_APP filme

RUN adduser -D adelina_docker

WORKDIR /home/adelina_docker

COPY app app
COPY templates templates
COPY static static
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY requirements.txt requirements.txt
COPY filme.py filme.py

RUN chmod +x dockerstart.sh

RUN python3 -m venv .venv && \
    .venv/bin/pip install --upgrade pip && \
    .venv/bin/pip install -r requirements.txt


USER adelina_docker

EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
