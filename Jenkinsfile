/*Jenkins*/
pipeline {
    agent any
    
    stages {
        stage('Clone repo') {
            steps {
	        git branch: 'dev_Corlan_Victor',
	        url: 'https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git'
	    }
	}
    
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    python3 -m venv .venv
		    . .venv/bin/activate		
		    pip install --upgrade pip
		    pip install -r quickrequirements.txt
                    '''
            }
        }
        
        stage('pylint - calitate cod') {
            agent any
            steps {
                sh '''
                    . ./activeaza_venv_jenkins;
                    echo '\n\nVerificare lib/*.py cu pylint\n';
                    pylint --exit-zero lib/*.py;

                    echo '\n\nVerificare tests/*.py cu pylint';
                    pylint --exit-zero tests/*.py;

                    echo '\n\nVerificare sysinfo.py cu pylint';
                    pylint --exit-zero filme.py;
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . ./activeaza_venv_jenkins;
		    pytest app/tests
                '''
            }
        }
        
        stage('Deploy') {
            agent any
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
                    docker build -t scc:v${BUILD_NUMBER} .
                    docker create --name scc${BUILD_NUMBER} -p 25568:25568 scc:v${BUILD_NUMBER}
                '''
            }
        }
    }
}
