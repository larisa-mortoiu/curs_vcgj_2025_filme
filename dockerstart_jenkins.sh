#!/bin/bash

# Nume container
CONTAINER_NAME=jenkins-docker

# Verifică dacă există deja un container cu același nume
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "Containerul $CONTAINER_NAME există deja. Îl pornesc..."
    docker start $CONTAINER_NAME
else
    echo "Pornez un container nou Jenkins cu acces la Docker..."
    docker run -d \
        --name $CONTAINER_NAME \
        -p 8080:8080 -p 50000:50000 \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v jenkins_home:/var/jenkins_home \
        jenkins/jenkins:lts
fi

echo "Accesează Jenkins la: http://localhost:8080"

