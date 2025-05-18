pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Construim imaginea Docker'
                sh 'docker build -t mechanicressurection .'
            }
        }

        stage('Run Container') {
            steps {
                echo 'Pornim containerul'
                sh '''
                    docker rm -f mechanicressurection || true
                    docker run -d -p 5000:5000 --name mechanicressurection mechanicressurection
                '''
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
