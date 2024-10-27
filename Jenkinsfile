// pipeline {
//     agent any

//     environment {
//         // Setting up the environment variable for database connection
//         DATABASE_URL = "postgresql://username:password@db:5432/dbname"
//         // Ensure PATH includes the directory where docker-compose is installed
//         PATH = "$PATH:/tmp"
//         DOCKER_HOST = 'tcp://host.docker.internal:2375' // Connects to Docker daemon over TCP
//     }

//     stages {
//         stage('Build') {
//             steps {
//                 script {
//                     if (isUnix()) {
//                         env.PATH = "$PATH:/usr/local/bin"  // For MacOS/Linux
//                     } else {
//                         env.PATH = "$PATH:/path/to/docker-compose"  // Windows-specific
//                     }
//                     sh 'docker-compose build' // build docker image
//                 }
//             }
//         }
//         stage('Debug') {
//             steps {
//                 dir('/var/jenkins_home/workspace/todolist-pipeline') {
//                     sh 'pwd'
//                     sh 'ls -l $(pwd)/prometheus.yml'
//                     sh 'cat $(pwd)/prometheus.yml'
//                 }
//             }
//         }
//         stage('Test') {
//             steps {
//                 script {
//                     try {
//                         // Running the test script inside the Docker container
//                         sh 'docker-compose run web python tests.py'
//                     } catch (Exception e) {
//                         sh 'docker-compose logs'
//                         error("Tests failed: ${e.getMessage()}") // show message if error
//                     }
//                 }
//             }
//         }
//         stage('Deploy') {
//             steps {
//                 // Deploying the application
//                 sh 'docker-compose up -d'
//             }
//             post {
//                 always {
//                     // This ensures the deployment stage runs regardless of previous stage results
//                     echo 'Deployment stage will run regardless of previous stage results'
//                 }
//             }
//         }
//     }
// }

pipeline {
    agent any

    environment {
        DATABASE_URL = "postgresql://username:password@db:5432/dbname"
        PATH = "$PATH:/tmp"
        DOCKER_HOST = 'tcp://host.docker.internal:2375'
    }

    stages {
        stage('Debug Jenkins Environment') {
            steps {
                script {
                    // Checking current directory
                    sh 'pwd'
                    sh 'ls -l /var/jenkins_home/workspace/todolist-pipeline/'

                    // Checking Docker version and permissions
                    sh 'docker --version'
                    sh 'docker ps'
                    sh 'id'
                }
            }
        }
        stage('Run Prometheus Directly') {
            steps {
                script {
                    try {
                        // Run Prometheus directly in a Jenkins pipeline to isolate issue
                        sh 'docker run --rm -d -p 9090:9090 --name test-prometheus prom/prometheus'
                        sh 'docker ps'
                    } catch (Exception e) {
                        sh 'docker logs test-prometheus'
                        error("Failed to run Prometheus container: ${e.getMessage()}")
                    }
                }
            }
        }
    }
}

