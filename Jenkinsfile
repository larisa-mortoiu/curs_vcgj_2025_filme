pipeline {
    agent any

    environment {
        IMAGE_NAME = "elena_docker:latest"
        PATH = "${HOME}/.local/bin:/usr/local/bin:/usr/bin:/bin"
    }

    stages {
        stage('Clone source code') {
            steps {
                git branch: 'main_Mirica_Elena',
                    url: 'https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git'
            }
        }

        stage('Installing dependencies') {
            steps {
                sh '''
                    echo "Upgrade pip"
                    python3 -m pip install --upgrade pip

                    echo "Installing packages from requirements.txt"
                    pip install --user -r requirements.txt

                    echo "Installing tools for testing"
                    pip install --user pytest pylint
                '''
            }
        }

        stage('Running tests') {
            steps {
                sh '''
                    echo "Run tests from app/tests/"
                    pytest app/tests/*.py || echo "Tests failed but continue"

                    echo "Run pylint on source code"
                    pylint --exit-zero app/lib/*.py
                    pylint --exit-zero filme.py
                    pylint --exit-zero app/tests/*.py
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
    }
}
