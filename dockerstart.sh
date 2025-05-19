#!/bin/bash

# Nume imagine și container
IMAGE_NAME="bobmarley"
CONTAINER_NAME="bobmarley_app"

# Oprește și șterge containerul vechi dacă există
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "🧹 Oprire și ștergere container vechi..."
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

# Build imaginea
echo "🔨 Build imagine Docker..."
docker build -t $IMAGE_NAME .

# Rulează containerul
echo "🚀 Pornire container Docker..."
docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME

echo "✅ Aplicația rulează pe: http://localhost:5000"

