pipeline {
    agent any

    stages {
        stage('Clone repo') {
            steps {
                git branch: 'dev_Anghelina_Mara',
                    url: 'https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git'
            }
        }

        stage('Set up Python') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/pytest'
            }
        }
    }

  
}
