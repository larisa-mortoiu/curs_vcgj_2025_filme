/*Jenkins*/
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
                    . ./activeaza_venv_jenkins
                '''
            }
        }

        stage('pylint - calitate cod') {
            agent any
            steps {
                sh '''
                    . ./activeaza_venv;

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
                    . ./activeaza_venv;
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
            docker rm -f flask-filme-container || true

            echo "Build imagine Docker"
            docker build -t flask-filme-image:v${BUILD_NUMBER} .

            echo "Pornire container pe portul 5011"
            docker run -d --name flask-filme-container -p 5011:5011 flask-filme-image:v${BUILD_NUMBER}

            echo "Container running:"
            docker ps | grep flask-filme
        '''
    }
}

    }
}
