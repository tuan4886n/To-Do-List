pipeline {
    agent any

    environment {
        // Setting up the environment variable for database connection
        DATABASE_URL = "postgresql://username:password@db:5432/dbname"
        PATH = "$PATH:/path/to/docker-compose"  // Ensure PATH includes the directory where docker-compose is installed
        DOCKER_HOST = 'tcp://host.docker.internal:2375'  // Connects to Docker daemon over TCP
    }

    stages {
        stage('Build') {
            steps {
                script {
                    if (isUnix()) {
                        env.PATH = "$PATH:/usr/local/bin"  // For MacOS/Linux
                    } else {
                        env.PATH = "$PATH:/path/to/docker-compose"  // Windows-specific
                    }
                    sh 'docker-compose build' // build docker image
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        // Running the test script inside the Docker container
                        sh 'docker-compose run web python test.py'
                    } catch (Exception e) {
                        echo "Test failure details:"
                        sh 'docker-compose logs'
                        error("Tests failed: ${e.getMessage()}")  // show messager if error
                    }
                }
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
