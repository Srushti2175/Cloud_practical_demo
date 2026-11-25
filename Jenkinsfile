
pipeline {
    agent any

    triggers {
        pollSCM('H/1 * * * *')
    }

    environment {
        IMAGE_NAME = 'srushti2175/jenkins-demo'
        EC2_HOST = '3.110.163.81'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Downloading source code'
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                echo 'Building Docker image'

                sh '''
                    docker build \
                    -t ${IMAGE_NAME}:${BUILD_NUMBER} \
                    -t ${IMAGE_NAME}:latest .
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing image to Docker Hub'

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login \
                        -u "$DOCKER_USER" --password-stdin

                        docker push ${IMAGE_NAME}:${BUILD_NUMBER}
                        docker push ${IMAGE_NAME}:latest

                        docker logout
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application to EC2'

                sshagent(credentials: ['ec2-ssh-key']) {

                    sh """
                        ssh -o StrictHostKeyChecking=no \
                        -o UserKnownHostsFile=/dev/null \
                        ec2-user@${EC2_HOST} \
                        'sudo docker pull ${IMAGE_NAME}:${BUILD_NUMBER} &&
                        (sudo docker rm -f jenkins-demo || true) &&
                        sudo docker run -d \
                        --name jenkins-demo \
                        --restart unless-stopped \
                        -p 80:5000 \
                        ${IMAGE_NAME}:${BUILD_NUMBER}'
                    """
                }
            }
        }
    }
}
