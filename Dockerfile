# syntax=docker/dockerfile:1

# 1. Base image
FROM python:3.12-alpine

# 2. Environment settings
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    FLASK_APP=filme.py \
    FLASK_RUN_HOST=0.0.0.0

# 3. Create a non-root user
RUN adduser -D filme

# 4. Switch to that user and set workdir
WORKDIR /home/filme/
USER filme

# 5. Copy application source (owned by filme)
COPY --chown=filme:filme app       app
COPY --chown=filme:filme static    static
COPY --chown=filme:filme templates templates
COPY --chown=filme:filme filme.py  filme.py

# 6. Back to root to set permissions & install OS deps
USER root
RUN chmod -R 755 static

# 7. Install curl for smoke tests
RUN apk add --no-cache curl

# 8. Create and activate venv, install Python deps
RUN python3 -m venv /home/filme/.venv
ENV PATH="/home/filme/.venv/bin:${PATH}"
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 9. Copy and make executable the entrypoint
COPY --chown=filme:filme dockerstart.sh dockerstart.sh
RUN chmod +x dockerstart.sh

# 10. Expose the Flask port
EXPOSE 5000

# 11. Entrypoint: run dockerstart.sh (launches Flask or any passed command)
ENTRYPOINT ["./dockerstart.sh"]

