pipeline {
  agent any

  environment {
    IMAGE_NAME = "jojo-scc-app"
    REGISTRY   = "docker.io/kais230/${IMAGE_NAME}"
  }

  stages {
    stage('Checkout') {
<<<<<<< HEAD
      steps {
        checkout scm
      }
=======
      steps { checkout scm }
>>>>>>> cdd6593 (updated jenkins and docker files)
    }

    stage('Unit Tests') {
      steps {
<<<<<<< HEAD
        sh 'pytest --maxfail=1 --disable-warnings -q'
=======
        script {
          // Run pytest inside a throw-away Python container
          docker.image('python:3.10-slim').inside {
            sh 'pip install --no-cache-dir -r requirements.txt'
            sh 'pytest --maxfail=1 --disable-warnings -q'
          }
        }
>>>>>>> cdd6593 (updated jenkins and docker files)
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
<<<<<<< HEAD
          // Build container tagged with the build number
=======
>>>>>>> cdd6593 (updated jenkins and docker files)
          dockerImage = docker.build("${IMAGE_NAME}:${env.BUILD_ID}")
        }
      }
    }

    stage('Smoke Test Container') {
      steps {
        script {
<<<<<<< HEAD
          // Run a temporary container and hit the root endpoint
=======
>>>>>>> cdd6593 (updated jenkins and docker files)
          dockerImage.inside('-p 5000:5000') {
            sh '''
              flask run --host=0.0.0.0 &
              sleep 5
              curl --fail http://localhost:5000
            '''
          }
        }
      }
    }

    stage('Push to Registry') {
<<<<<<< HEAD
      when {
        branch 'main'
      }
=======
      when { branch 'main_Al-Hajjih_Kais' }
>>>>>>> cdd6593 (updated jenkins and docker files)
      steps {
        withCredentials([
          usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'DOCKER_USER',
            passwordVariable: 'DOCKER_PASS'
          )
        ]) {
          sh '''
            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
            docker tag ${IMAGE_NAME}:${env.BUILD_ID} ${REGISTRY}:latest
            docker push ${REGISTRY}:latest
          '''
        }
      }
    }
  }

<<<<<<< HEAD
  post {
    always {
      cleanWs()
    }
  }
=======
  post { always { cleanWs() } }
>>>>>>> cdd6593 (updated jenkins and docker files)
}

