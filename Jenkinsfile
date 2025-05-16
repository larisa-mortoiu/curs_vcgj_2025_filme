pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Preluăm codul sursă'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Construim imaginea Docker'
                sh 'docker build -t lucifer-app .'
            }
        }

        stage('Run Container') {
            steps {
                echo 'Pornim containerul'
                sh 'docker run -d -p 5000:5000 lucifer-app'
            }
        }

        stage('List Running Containers') {
            steps {
                echo 'Listăm containerele active'
                sh 'docker ps'
            }
        }
    }
}
