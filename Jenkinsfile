pipeline {
    agent any

    environment {
        VENV_ACTIVATION = '. ./activeaza_venv'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
                    ${VENV_ACTIVATION}
                '''
            }
        }

        stage('Calitate cod - pylint') {
            steps {
                echo 'Rulare pylint pe lib și tests'
                sh '''
                    ${VENV_ACTIVATION}
                    echo '\n\nVerificare app/lib/*.py cu pylint\n'
                    pylint --exit-zero app/lib/*.py || true

                    echo '\n\nVerificare app/tests/*.py cu pylint\n'
                    pylint --exit-zero app/tests/*.py || true
                '''
            }
        }

        stage('Testare unitară - pytest') {
            steps {
                echo 'Rulez testele cu pytest...'
                sh '''
                    ${VENV_ACTIVATION}
                    pytest app/tests/
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'În lucru...'
            }
        }
    }
}
