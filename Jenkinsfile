pipeline {
    agent any

    environment {
        // Setting up the environment variable for database connection
        DATABASE_URL = "postgresql://tuan:tuanpham123@localhost/todolist"
        PATH = "$PATH:/tmp"  // Ensure PATH includes the directory where docker-compose is installed
        DOCKER_HOST = 'tcp://host.docker.internal:2375'  // Connects to Docker daemon over TCP
    }

    stages {
        stage('Build') {
            steps {
                // Building the Docker image 
                sh 'docker-compose build'
            }
        }
        stage('Test') {
            steps {
                // Running the test script inside the Docker container
                sh 'docker-compose run web python tests.py'
            }
        }
        stage('Deploy') {
            steps {
                // Deploying the application 
                sh 'docker-compose up -d'
            }
            post {
                always {
                    // This ensures the deployment stage runs regardless of previous stage results
                    echo 'Deployment stage will run regardless of previous stage results'
                }
            }
        }
    }
}
