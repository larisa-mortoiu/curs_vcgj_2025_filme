pipeline {
  agent any

  environment {
    IMAGE_NAME = "jojo-scc-app"
    IMAGE_TAG  = "${IMAGE_NAME}:${env.BUILD_NUMBER}"
    REGISTRY   = "docker.io/kais230/${IMAGE_NAME}"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        echo "Building ${IMAGE_TAG}"
        sh "docker build -t ${IMAGE_TAG} ."
      }
    }

    stage('Unit Tests (inside container)') {
      steps {
        echo "Running pytest inside ${IMAGE_TAG}"
        sh "docker run --rm ${IMAGE_TAG} pytest -q --maxfail=1"
      }
    }

    stage('Smoke Test Container') {
      steps {
        echo "Starting container for smoke test"
        sh """
          docker run -d --name smoke-test -p 5000:5000 ${IMAGE_TAG}
          sleep 5
          curl --fail http://localhost:5000
          docker stop smoke-test
          docker rm smoke-test
        """
      }
    }

    stage('Push to Registry') {
      when { branch 'main' }
      steps {
        withCredentials([usernamePassword(
          credentialsId: 'dockerhub-creds',
          usernameVariable: 'DOCKER_USER',
          passwordVariable: 'DOCKER_PASS'
        )]) {
          echo "Pushing ${IMAGE_TAG} → ${REGISTRY}:latest"
          sh """
            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
            docker tag ${IMAGE_TAG} ${REGISTRY}:latest
            docker push ${REGISTRY}:latest
          """
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

