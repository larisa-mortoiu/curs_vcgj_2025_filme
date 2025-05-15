FROM python:3.11-alpine

ENV FLASK_APP filme

#create a new user for security reasons
RUN adduser -D elena_docker

USER elena_docker

WORKDIR /home/elena_docker

COPY app app
COPY templates templates
COPY static static
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY requirements.txt requirements.txt
COPY filme.py filme.py

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r requirements.txt

#runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]