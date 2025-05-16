pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "adelina_docker:latest"
    }

    stages {
        stage('Clone repo') {
            agent any
            steps {
                git branch: 'main_Constantinescu_Adelina',
                    url: 'https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git'
            }
        }

        stage('Install & Test & Lint') {
            agent any
            steps {
                sh '''
                    export PATH=$HOME/.local/bin:$PATH

                    echo "Instalare pachete..."
                    pip install --upgrade pip
                    pip install --user -r requirements.txt
                    pip install --user pytest pylint

                    echo "Rulare teste cu pytest"
                    pytest app/tests/*.py || true

                    echo "Verificare cod cu pylint"
                    pylint --exit-zero app/lib/*.py
                    pylint --exit-zero filme.py
                    pylint --exit-zero app/tests/*.py
                '''
            }
        }
    }
}
