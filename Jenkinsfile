pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t mechanicressurection .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                    docker rm -f mechanicressurection || true
                    docker run -d -p 5000:5000 --name mechanicressurection mechanicressurection
                '''
            }
        }

        stage('Check Container') {
            steps {
                sh 'docker ps'
            }
        }
    }
}
