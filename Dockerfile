FROM python:3.6

ENV FLASK_APP filme

RUN adduser scc

USER scc

WORKDIR /home/scc

COPY app app
COPY templates templates
COPY static static
COPY activeaza_venv activeaza_venv
COPY activeaza_venv_jenkins activeaza_venv_jenkins
COPY dockerstart.sh dockerstart.sh
USER root
RUN chmod a+x dockerstart.sh
RUN chmod a+x activeaza_venv
RUN chmod a+x activeaza_venv_jenkins
USER scc
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY filme.py filme.py

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt

#runtime configuration
EXPOSE 25568
ENTRYPOINT ["./dockerstart.sh"]