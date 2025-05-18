pipeline {
    agent any

    environment {
        IMAGE_NAME = 'filme_app'
        CONTAINER_NAME = 'filme_app'
        HOST_PORT = '5000'
        CONTAINER_PORT = '5000'
    }

    stages {
        stage('Checkout') {
            steps {
                // Folosește repo-ul și branch-ul setat în Jenkins job
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${IMAGE_NAME}"
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Remove Old Container') {
            steps {
                echo "Removing old container if exists..."
                sh "docker rm -f ${CONTAINER_NAME} || true"
            }
        }

        stage('Run Container') {
            steps {
                echo "Running new container..."
                sh "docker run -d -p ${HOST_PORT}:${CONTAINER_PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}"
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully!'
        }
        failure {
            echo 'Pipeline failed. Check console output for details.'
        }
    }
}
