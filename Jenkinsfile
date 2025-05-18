pipeline {
    agent any

    environment {
        VENV = "${WORKSPACE}/venv"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Clonăm proiectul'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Creăm mediu virtual și instalăm dependințele'
                sh '''
                    python3 -m venv $VENV
                    . $VENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Rulăm testele cu pytest'
                sh '''
                    . $VENV/bin/activate
                    export PYTHONPATH=$WORKSPACE
                    pytest tests/
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Construim imaginea Docker'
                sh 'docker build -t lucifer-app .'
            }
        }

        stage('Run Container') {
            steps {
                echo 'Pornim containerul'
                sh 'docker run -d -p 5000:5000 --name lucifer_temp lucifer-app'
            }
        }

        stage('Verify Container is Running') {
            steps {
                sh 'docker ps | grep lucifer-app'
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Oprim și ștergem containerul'
                sh '''
                    docker stop lucifer_temp || true
                    docker rm lucifer_temp || true
                '''
            }
        }
    }

    post {
        failure {
            echo 'Build eșuat. Curățăm eventualul container rămas.'
            sh '''
                docker stop lucifer_temp || true
                docker rm lucifer_temp || true
            '''
        }
    }
}
