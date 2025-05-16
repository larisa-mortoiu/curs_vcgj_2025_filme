pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/<user>/curs_vcgj_2025_filme.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t lucifer-app .'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'pytest tests/'  // dacă ai teste
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 lucifer-app'
            }
        }
    }
}
