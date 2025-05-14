pipeline {
    agent any

    environment {
        VENV_DIR = ".venv"
        ACTIVATE = ". .venv/bin/activate"
    }

    stages {
        stage('Clone repo') {
            steps {
                git branch: 'dev_Dina_Alexandra',
                    url: 'https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git'
            }
        }

        stage('Set up virtual environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Code Quality - pylint') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    echo ' Verificare cod din app/lib/ cu pylint'
                    pylint --exit-zero app/lib/*.py || true

                    echo ' Verificare teste din app/tests/ cu pylint'
                    pylint --exit-zero app/tests/*.py || true

                    echo ' Verificare filme.py cu pylint'
                    pylint --exit-zero filme.py || true
                '''
            }
        }

        stage('Run Tests - pytest') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest app/tests
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Etapa de deploy – în lucru...'
            }
        }
    }
}
