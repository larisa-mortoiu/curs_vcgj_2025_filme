pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install flask pytest'
            }
        }

	stage('Code quality check') {
    	    steps {
        	sh 'pylint --exit-zero filme.py app/lib/*.py app/tests/*.py'
    	    }
	}

        stage('Run tests') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}
