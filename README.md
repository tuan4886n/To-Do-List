# To-Do List Application

## Overview
A simple to-do list application developed with Flask and PostgreSQL, containerized in Docker, and monitored with Prometheus and Grafana.
![image](https://github.com/user-attachments/assets/fb43c8db-7794-4bd4-8f13-7201b5d2ab3c)

## Technologies Used
- Flask
- PostgreSQL
- Docker, Docker Compose
- Prometheus
- Grafana
- Jenkins for CI/CD

## Prerequisites
- [Docker and Docker Compose installed](https://docs.docker.com/get-docker/)
- [Python 3.x installed](https://www.python.org/downloads/)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/tuan4886n/To-Do-List.git
cd To-Do-List

```

### 2. Set Up Environment Variables
- Create a .env file from the example.env file and update it with your settings:
```bash
cp example.env .env

```

### 3. Build and Run the Application
```bash
docker-compose up --build

```
#### Running Tests
- To run the tests, execute:

```bash
docker-compose run web python test.py

```
### Monitoring
- Prometheus available at http://localhost:9090
  ![image](https://github.com/user-attachments/assets/b08fb2ee-f306-44d2-b646-6a4753552e47)
- Grafana available at http://localhost:3000
  ![image](https://github.com/user-attachments/assets/57d97342-b033-475c-9226-7564539f9f2c)

login with username: **admin**, password: **admin**
### Grafana Setup
- Add Prometheus as a data source in Grafana
- In section Prometheus server URL : input http://prometheus:9090
![image](https://github.com/user-attachments/assets/6d6085bf-eb4c-4d36-a862-d108300b7e5f)
- Create dashboards to visualize metrics (remember select data source : Prometheus)

### Jenkins Pipeline
#### Prerequisites
- Ensure Jenkins is set up to run Docker containers and has access to your .env configuration.
- Install necessary Jenkins plugins:
  - Docker Pipeline Plugin
  - Pipeline: GitHub Plugin
  - GitHub Integration Plugin
#### Steps
##### 1. Set Up Jenkins Job:
- Create a new Jenkins job.
- Choose "Pipeline" as the job type.
##### 2. Configure GitHub Repository
- In the job configuration, under "Pipeline", configure the repository settings:
  - Repository URL: your repository (example https://github.com/tuan4886n/To-Do-List.git)
  - Credentials: Add your GitHub credentials if required.
##### 3. Example Jenkinsfile:
- Using the Jenkinsfile above in my repository to define the pipeline
##### 4. Triggering Builds:
- Configure triggers in Jenkins to automatically build on changes to the GitHub repository.
#### Monitoring Builds
- Monitor the Jenkins job console output to ensure each stage completes successfully.
- Check logs and resolve any issues if a build fails.
