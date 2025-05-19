#!/bin/bash
echo " Build Docker image..."
docker build -t dexter_app .

echo " Run Docker container on port 5000..."
docker run -p 5000:5000 dexter_app

