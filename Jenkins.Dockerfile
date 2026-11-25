FROM jenkins/jenkins:lts-jdk21

USER root

RUN apt-get update && \
    apt-get install -y docker.io openssh-client git && \
    rm -rf /var/lib/apt/lists/*

USER root
