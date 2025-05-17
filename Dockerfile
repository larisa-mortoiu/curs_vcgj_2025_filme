# syntax=docker/dockerfile:1
FROM python:3.12-alpine

# ensure a consistent C locale
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    FLASK_APP=filme.py \
    FLASK_RUN_HOST=0.0.0.0

# create non-root user
RUN adduser -D filme
WORKDIR /home/filme/
USER filme

# copy source
COPY --chown=filme:filme app       app
COPY --chown=filme:filme static    static
COPY --chown=filme:filme templates templates
COPY --chown=filme:filme filme.py  filme.py

# back to root to setup venv & perms
USER root
RUN chmod -R 755 static

# create venv and install deps
RUN python3 -m venv /home/filme/.venv
ENV PATH="/home/filme/.venv/bin:${PATH}"
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy entrypoint
COPY --chown=filme:filme dockerstart.sh dockerstart.sh
RUN chmod +x dockerstart.sh

EXPOSE 5000

ENTRYPOINT ["./dockerstart.sh"]

