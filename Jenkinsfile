pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "elena_docker:latest"
    }

    stages {
        stage('Clone repo') {
            steps {
                git branch: 'main_Mirica_Elena',
                    url: 'https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git'
            }
        }

        stage('Build') {
            steps {
               sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Code quality') {
            steps {
                sh '''
                    . ./activeaza_venv;
                    echo '\n\nVerificare lib/*.py cu pylint\n';
                    pylint --exit-zero lib/*.py;

                    echo '\n\nVerificare tests/*.py cu pylint';
                    pylint --exit-zero tests/*.py;

                    echo '\n\nVerificare filme.py cu pylint';
                    pylint --exit-zero filme.py;
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/pytest'
            }
        }
    }
  
}