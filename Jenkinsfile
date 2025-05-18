/* Jenkins */

pipeline {
    agent any

    stages {
        stage('Build') {
            agent any
            steps {
                echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
                    . ./activeazavenvjenkins
                '''
            }
        }

        stage('pylint - calitate cod') {
            agent any
            steps {
                sh '''
                    . ./activeazavenv;

                    echo '\n\nVerificare test_filme.py cu pylint';
                    pylint --exit-zero app/tests/test_filme.py;

                    echo '\n\nVerificare filme.py cu pylint';
                    pylint --exit-zero filme.py;
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . ./activeazavenv;
                    pytest;
                '''
            }
        }

        stage('Deploy') {
            agent any
            steps {
                echo 'Deploy: build & run container Docker'
                sh '''
                    echo "Oprire container vechi (dacă există)"
                    docker rm -f theblacklist-container || true

                    echo "Build imagine Docker"
                    docker build -t theblacklist-image:v${BUILD_NUMBER} .

                    echo "Pornire container pe portul 5077"
                    docker run -d --name theblacklist-container -p 5077:5077 theblacklist-image:v${BUILD_NUMBER}

                    echo "Container running:"
                    docker ps | grep theblacklist
                '''
            }
        }
    }
}

