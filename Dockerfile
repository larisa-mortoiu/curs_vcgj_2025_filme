# 1. Use Alpine-based Python for a small image
FROM python:3.12-alpine

# 2. Tell Flask which module to run
ENV FLASK_APP=filme.py
ENV FLASK_RUN_HOST=0.0.0.0

# 3. Create an unprivileged user
RUN adduser -D filme

# 4. Switch into that user for the bulk of the build
USER filme
WORKDIR /home/filme/

# 5. Copy your application code
COPY app     app
COPY static  static
COPY templates templates
COPY filme.py filme.py

# 6. Back to root to set permissions & prepare venv
USER root
RUN chmod -R 777 static

# 7. Create and configure a virtual environment
RUN python3 -m venv .venv
RUN chmod -R g+x .venv

# 8. Copy your dependencies spec
COPY requirements.txt requirements.txt
# (Also copy pytest.ini if you have one:)
# COPY pytest.ini pytest.ini

# 9. Ensure your startup script is executable
COPY dockerstart.sh dockerstart.sh
RUN chmod +x dockerstart.sh

# 10. Install Python deps into the venv
RUN .venv/bin/pip install --no-cache-dir -r requirements.txt

# 11. Expose the port your Flask app listens on (default 5000)
EXPOSE 5000

# 12. When the container starts, run your launch script
ENTRYPOINT ["./dockerstart.sh"]

