FROM ubuntu:latest

#LABEL stifix

COPY . /site/
WORKDIR /

RUN apt update && \
 apt install -y npm nodejs-legacy && \
 npm list harp || npm install harp -g

EXPOSE 9000

CMD harp server site
