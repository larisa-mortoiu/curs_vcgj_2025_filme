pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install flask pytest'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}
