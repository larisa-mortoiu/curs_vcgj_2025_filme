pipeline {
  agent any

  environment {
    IMAGE       = "jojo-scc-app"
    TAG         = "${IMAGE}:${BUILD_NUMBER}"
    REMOTE      = "docker.io/kais230/${IMAGE}"
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Build Image') {
      steps {
        sh "docker build -t ${TAG} ."
      }
    }

    stage('Unit Tests (in-container)') {
      steps {
        // override ENTRYPOINT so dockerstart.sh runs pytest
        sh "docker run --rm --entrypoint sh ${TAG} -c \"./dockerstart.sh pytest -q --maxfail=1\""
      }
    }

    stage('Smoke Test') {
      steps {
        sh """
          docker run -d --name smoke-${BUILD_NUMBER} -p 5000:5000 ${TAG}
          timeout 10 sh -c 'until curl -s http://localhost:5000 >/dev/null; do sleep 1; done'
          curl --fail http://localhost:5000
          docker stop smoke-${BUILD_NUMBER}
          docker rm smoke-${BUILD_NUMBER}
        """
      }
    }

    stage('Push to Hub') {
      when { branch 'main' }
      steps {
        withCredentials([usernamePassword(
          credentialsId: 'dockerhub-creds',
          usernameVariable: 'DOCKER_USER',
          passwordVariable: 'DOCKER_PASS'
        )]) {
          sh """
            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
            docker tag ${TAG} ${REMOTE}:latest
            docker push ${REMOTE}:latest
          """
        }
      }
    }
  }

  post {
    always { cleanWs() }
  }
}

