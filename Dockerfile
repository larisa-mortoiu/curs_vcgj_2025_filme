FROM python:3.11-alpine

ENV FLASK_APP=filme.py
ENV FLASK_RUN_PORT=5011
ENV FLASK_ENV=development

# Create a non-root user
RUN adduser -D hoang_docker
USER hoang_docker

WORKDIR /home/hoang_docker

# Copy application files
COPY app app
COPY templates templates
COPY static static
COPY filme.py filme.py
COPY requirements.txt requirements.txt
COPY pytest.ini pytest.ini
COPY dockerstart.sh dockerstart.sh

# Set up virtual environment
RUN python3 -m venv .venv && \
    .venv/bin/pip install --upgrade pip && \
    .venv/bin/pip install -r requirements.txt

# Runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]

