<<<<<<< HEAD
# Use a minimal Python base image
FROM python:3.10-slim

# Set working directory inside the container
=======
# Dockerfile
FROM python:3.10-slim

>>>>>>> cdd6593 (updated jenkins and docker files)
WORKDIR /app

# Install runtime dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

<<<<<<< HEAD
# Copy the rest of your application
COPY . .

# Tell Flask how to start
ENV FLASK_APP=filme.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port your app runs on
EXPOSE 5000

# Default command
=======
# Copy app sources
COPY . .

# Tell Flask how to run
ENV FLASK_APP=filme.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

>>>>>>> cdd6593 (updated jenkins and docker files)
CMD ["flask", "run"]

