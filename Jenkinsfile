pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source…'
                checkout scm
            }
        }

		stage('Setup & Unit Tests') {
	  steps {
	    echo 'Creating venv, installing deps & running pytest…'
	    sh '''
		  pip3 install --user -r requirements.txt pytest
		  pytest --maxfail=1 --disable-warnings -q
		'''
	  }
	}

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: jojo-scc-app:v${BUILD_NUMBER}"
                sh '''
                  docker build -t jojo-scc-app:v${BUILD_NUMBER} .
                '''
            }
        }

        stage('Smoke Test Container') {
            steps {
                echo 'Starting container and hitting /…'
                sh '''
                  docker run -d --name smoke-test-${BUILD_NUMBER} -p 5000:5000 jojo-scc-app:v${BUILD_NUMBER}
                  sleep 5
                  curl --fail http://localhost:5000
                  docker stop smoke-test-${BUILD_NUMBER}
                  docker rm smoke-test-${BUILD_NUMBER}
                '''
            }
        }

        stage('Push to Registry') {
            when { branch 'main' }
            steps {
                echo 'Logging in & pushing to Docker Hub…'
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                      docker tag jojo-scc-app:v${BUILD_NUMBER} docker.io/kais230/jojo-scc-app:latest
                      docker push docker.io/kais230/jojo-scc-app:latest
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning workspace…'
            cleanWs()
        }
    }
}

