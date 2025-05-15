/* Jenkins */
pipeline {
    agent any

    stages {
        stage('Build Project') {
            steps {
                echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
                    . ./activeaza_venv_jenkins
                '''
            }
        }

        stage('Cod-Quality Check') {
            steps {
                sh '''
                    . ./activeaza_venv

                    echo '\n\nVerificare app/lib/*.py cu pylint\n';
                    pylint --exit-zero app/lib/*.py;

                    echo '\n\nVerificare app/tests/*.py cu pylint';
                    pylint --exit-zero app/tests/*.py;

                    echo '\n\nVerificare filme.py cu pylint';
                    pylint --exit-zero filme.py;
                '''
            }
        }

        stage('Run Unit Test pytest') {
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . ./activeaza_venv
                    pytest --maxfail=1
                '''
            }
        }

        stage('Docker Image Creation') {
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
                    docker build -t movieimage:v${BUILD_NUMBER} .
                    docker create --name moviecontainer${BUILD_NUMBER} -p 8020:5011 movieimage:v${BUILD_NUMBER}
                '''
            }
        }
    }
}
