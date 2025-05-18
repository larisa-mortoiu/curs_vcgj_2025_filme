pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'dev_Simion_Razvan', url: 'https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t filme_app .'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 --name filme_app filme_app || true'
                }
            }
        }
    }
}
