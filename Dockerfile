# Use a minimal Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application
COPY . .

# Tell Flask how to start
ENV FLASK_APP=filme.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port your app runs on
EXPOSE 5000

# Default command
CMD ["flask", "run"]

