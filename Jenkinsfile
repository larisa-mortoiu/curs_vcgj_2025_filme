pipeline {
    agent any

    environment {
        VENV_DIR = ".venv"
        ACTIVATE = ". .venv/bin/activate"
    }

    stages {
        stage('Clone repo') {
            steps {
                git branch: 'dev_Pham_Hoang', 
                    url: 'https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git'
            }
        }

        stage('Set up virtual environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Code Quality - pylint') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    echo ' Verificare app/lib/*.py'
                    pylint --exit-zero lib/*.py;

                    echo ' Verificare app/tests/*.py'
                    pylint --exit-zero tests/*.py;

                    echo ' Verificare filme.py'
                    pylint --exit-zero filme.py;
                '''
            }
        }

        stage('Run Tests - pytest') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    pytest app/tests
                '''
            }
        }

        stage('Deploy - Build Docker Image') {
            steps {
                echo " Build ID: ${BUILD_NUMBER}"
                sh '''
                    docker build -t movieimage:v${BUILD_NUMBER} .

                    docker create --name moviecontainer${BUILD_NUMBER} -p 8020:5011 movieimage:v${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        always {
            echo " Pipeline terminat!"
            sh "docker ps -a"
        }
    }
}

