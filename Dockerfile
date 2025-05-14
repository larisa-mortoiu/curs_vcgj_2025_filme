FROM python:3.12-alpine

ENV FLASK_APP filme
#ENV FLASK_CONFIG = docker

#3.12 alpine
RUN adduser -D filme

USER filme

WORKDIR /home/filme/

COPY app app
COPY static static
COPY templates templates
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY filme.py filme.py

USER root   
RUN chmod -R 777 static

RUN python3 -m venv .venv
RUN chmod -R g+x .venv
RUN chmod +x dockerstart.sh

RUN .venv/bin/pip install -r quickrequirements.txt


# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
#CMD sh