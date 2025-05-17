# Use a minimal Python image
FROM python:3.10-slim

# Set a working directory
WORKDIR /app

# Install build-time dependencies (if any) and your Python libs
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY . .

# Expose Flask port and set env vars
ENV FLASK_APP=filme.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

# Default command to start your app
CMD ["flask", "run"]
