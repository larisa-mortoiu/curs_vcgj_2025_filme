pipeline {
    agent any

    stages {
        stage('Install deps') {
            steps {
                sh 'pip install flask'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest app/tests'
            }
        }
    }
}
