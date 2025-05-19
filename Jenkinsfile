pipeline {
    agent any

    environment {
        VENV_PATH = '.venv_jenkins'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Se preia codul sursă...'
                checkout scm
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                echo '🛠️ Se pregătește mediul virtual...'
                sh 'chmod +x activeaza_venv_jenkins'
                sh './activeaza_venv_jenkins'
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Se rulează testele...'
                sh """
                    . ${VENV_PATH}/bin/activate
                    pytest app/tests/test_file.py
                """
            }
        }

        stage('Run App (opțional)') {
            when {
                expression { return params.RUN_APP == true }
            }
            steps {
                echo '🚀 Se pornește aplicația...'
                sh """
                    source ${VENV_PATH}/bin/activate
                    nohup python filme.py &
                """
            }
        }
    }

    post {
        always {
            echo '📦 Build terminat.'
        }
        failure {
            echo '❌ Build eșuat.'
        }
        success {
            echo '✅ Build reușit.'
        }
    }
}

