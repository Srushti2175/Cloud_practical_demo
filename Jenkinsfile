
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Downloading source code'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image'
            }
        }

        stage('Push') {
            steps {
                echo 'Pushing image to Docker Hub'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application to EC2'
            }
        }
    }
}
