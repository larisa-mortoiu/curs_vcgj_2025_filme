pipeline {
    agent any

    environment {
        VENV_DIR = ".venv"
        ACTIVATE = ".venv/bin/activate"
    }

    stages {
        stage('Clone repo') {
            steps {
                git branch: 'main', url: 'https://github.com/USER/REPO.git'
            }
        }

        stage('Set up Python venv') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run lint') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pylint app/ filme.py || true
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest app/tests/test_filme.py --maxfail=1 --disable-warnings -q
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
    }
}

