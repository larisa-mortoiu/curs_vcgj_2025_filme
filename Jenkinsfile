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
    echo "Smoke–testing inside container ${TAG}"
    // run your dockerstart.sh inside the container, then curl localhost:5000
    sh """
      docker run --rm --entrypoint sh ${TAG} -c \\
        "./dockerstart.sh & \\
         sleep 5 && \\
         curl --fail http://127.0.0.1:5000"
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

