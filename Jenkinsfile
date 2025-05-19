pipeline {
    agent any

    environment {
        VENV_DIR = ".venv"
    }

    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.11-alpine'
                    args '-u root'
                }
            }
            steps {
                echo 'Building...'
                sh '''
                    apk add --no-cache python3-dev py3-pip py3-virtualenv gcc musl-dev

                    echo "Creez mediul virtual în .venv"
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate

                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('pylint - calitate cod') {
            agent {
                docker {
                    image 'python:3.11-alpine'
                    args '-u root'
                }
            }
            steps {
                sh '''
                    apk add --no-cache python3-dev py3-pip py3-virtualenv gcc musl-dev

                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install -r requirements.txt
                    pip install pylint

                    echo '\n\nVerificare test_filme.py cu pylint'
                    pylint --exit-zero app/tests/test_filme.py

                    echo '\n\nVerificare filme.py cu pylint'
                    pylint --exit-zero filme.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            agent {
                docker {
                    image 'python:3.11-alpine'
                    args '-u root'
                }
            }
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    apk add --no-cache python3-dev py3-pip py3-virtualenv gcc musl-dev

                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install -r requirements.txt
                    pip install pytest

                    pytest
                '''
            }
        }

        stage('Deploy') {
            agent any
            steps {
                echo 'Deploy: build & run container Docker'
                sh '''
                    echo "Oprire container vechi (dacă există)"
                    docker rm -f flask-filme-container || true

                    echo "Build imagine Docker"
                    docker build -t flask-filme-image:v${BUILD_NUMBER} .

                    echo "Pornire container pe portul 5011"
                    docker run -d --name flask-filme-container -p 5011:5011 flask-filme-image:v${BUILD_NUMBER}

                    echo "Container running:"
                    docker ps | grep flask-filme
                '''
            }
        }
    }
}

