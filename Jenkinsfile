pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t darkimage:v1 .'
            }
        }

        stage('pylint - calitate cod') {
            steps {
                echo 'Running pylint...'
                sh '''
                    echo "--- Lint app/lib/"
                    pylint --exit-zero app/lib/*.py

                    echo "--- Lint app/tests/"
                    pylint --exit-zero app/tests/*.py

                    echo "--- Lint filme.py"
                    pylint --exit-zero filme.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Running unit tests...'
                sh 'PYTHONPATH=/app pytest app/tests/'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Running container on port 8020...'
                sh '''
                    docker rm -f darkcontainer || true
                    docker run -d --name darkcontainer -p 8020:5000 darkimage:v1
                '''
            }
        }
    }
}
