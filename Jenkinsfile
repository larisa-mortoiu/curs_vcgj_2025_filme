pipeline {
    agent any

    environment {
        VENV_PATH = '.venv_jenkins'
    }

    parameters {
        booleanParam(name: 'RUN_APP', defaultValue: false, description: 'Rulează aplicația Flask după testare?')
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
                // Testează toate fișierele din folder
                sh './.venv_jenkins/bin/pytest app/tests/'
            }
        }

        stage('Run App (opțional)') {
            when {
                expression { return params.RUN_APP == true }
            }
            steps {
                echo '🚀 Se pornește aplicația Flask...'
                sh 'nohup ./.venv_jenkins/bin/python3 filme.py &'
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

