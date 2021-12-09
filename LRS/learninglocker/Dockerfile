# Consult http://docs.learninglocker.net/guides-custom-installation/
FROM ubuntu:18.04
SHELL ["/bin/bash", "-c"]
RUN apt-get update && \
    apt-get -y install curl git python build-essential xvfb apt-transport-https

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install -y nodejs && \
    source ~/.bashrc && \
    npm install -g yarn && \
    npm install -g pm2 && \
    pm2 install pm2-logrotate && \
    pm2 set pm2-logrotate:compress true

# Install and build the Learning Locker UI, API, and Worker
WORKDIR /usr/local/src
RUN git clone https://github.com/LearningLocker/learninglocker.git 

WORKDIR /usr/local/src/learninglocker
COPY .env.learninglocker .env

RUN source ~/.bashrc && \
    npm_config_build_from_source=true yarn add google-gax --ignore-engines && \
    yarn install --ignore-engines && \
    yarn build-all

# Install xAPI service
WORKDIR /usr/local/src
RUN git clone https://github.com/LearningLocker/xapi-service.git 

WORKDIR /usr/local/src/xapi-service
COPY .env.xapi-service .env
RUN source ~/.bashrc && \
    yarn install --ignore-engines && \
    yarn build
