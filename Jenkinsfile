pipeline {
  agent any

  environment {
    IMAGE_NAME = "jojo-scc-app"
    REGISTRY   = "docker.io/kais230/${IMAGE_NAME}"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Unit Tests') {
      steps {
        sh 'pytest --maxfail=1 --disable-warnings -q'
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          // Build container tagged with the build number
          dockerImage = docker.build("${IMAGE_NAME}:${env.BUILD_ID}")
        }
      }
    }

    stage('Smoke Test Container') {
      steps {
        script {
          // Run a temporary container and hit the root endpoint
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
      when {
        branch 'main'
      }
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

  post {
    always {
      cleanWs()
    }
  }
}

