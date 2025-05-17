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
                    echo '\n\nVerificare lib/*.py cu pylint\n';
                    pylint --exit-zero lib/*.py;

                    echo '\n\nVerificare tests/*.py cu pylint';
                    pylint --exit-zero tests/*.py;

                    echo '\n\nVerificare sysinfo.py cu pylint';
                    pylint --exit-zero sysinfo.py;
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
        /*    }
        }*/
        stage('Deploy') {
    agent any
    steps {
        echo "🚀 Deploy: build & run container Docker"

        sh '''
            echo "🔁 Oprire container vechi (dacă există)"
            docker rm -f breakingbad-container || true

            echo "🐳 Build imagine Docker"
            docker build -t breakingbad-image:v${BUILD_NUMBER} .

            echo "🚀 Pornire container pe portul 5011"
            docker run -d --name breakingbad-container -p 5011:5011 breakingbad-image:v${BUILD_NUMBER}

            echo "📦 Container running:"
            docker ps | grep breakingbad
        '''
    }
}
    
}
