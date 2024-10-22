pipeline{
    agent any

    environment{
        // setting up the evironment for database
        DATABASE_URL= "postgresql://tuan:tuanpham123@localhost/todolist"  
    }

    stages{
        stage('Build'){
            step{
                // build the docker image
                sh 'docker-compose build'
            }   
        }
        stage('Test'){
            step{
                // Running test the script inside docker container
                sh 'docker-compose run web python test.py'
            }
        }
        stage('Deploy'){
            step{
                // deploy the application
                sh 'docker-compose up -d'
            }
        }
    }
}