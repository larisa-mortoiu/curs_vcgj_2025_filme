pipeline {
    agent any

    environment {
        IMAGE_NAME = "filme-app"
        IMAGE_TAG = "v${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Preluare cod sursă...'
                checkout scm
            }
        }

        stage('Setup venv și install requirements') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r quickrequirements.txt
                '''
            }
        }

        stage('Linter - pylint') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pylint filme.py || true
                '''
            }
        }

        stage('Unit Tests - pytest') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest app/tests || true
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Docker Run (opțional)') {
            steps {
                sh '''
                    docker run -d --name filme_container_${BUILD_NUMBER} -p 5050:5050 ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }
    }

    post {
        success {
            echo 'Build, test și dockerizare reușite.'
        }
        failure {
            echo 'A apărut o eroare în pipeline.'
        }
    }
}
