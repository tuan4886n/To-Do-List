pipeline {
    agent any

    environment {
        // setting up environment for database
        DATABASE_URL = "postgresql://tuan:tuanpham123@localhost/todolist"
    }

    stages {
        stage('Build') {
            steps {
                // build the docker image
                sh 'docker-compose build'
            }
        }
        stage('Test') {
            steps {
                // Running test the script inside docker container
                sh 'docker-compose run web python tests.py'
            }
        }
        stage('Deploy') {
            steps {
                // deploy the application
                sh 'docker-compose up -d'
            }
        }
    }
}
