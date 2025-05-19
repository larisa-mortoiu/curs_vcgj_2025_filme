pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest app/tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t twilight-app .'
            }
        }

        stage('Run Container (optional)') {
            when {
                expression { return env.RUN_CONTAINER == 'true' }
            }
            steps {
                sh 'docker run -d -p 5000:5000 --name twilight-app twilight-app'
            }
        }
    }
}
