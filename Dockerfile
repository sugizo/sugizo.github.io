FROM ubuntu:latest

#MAINTAINER Stifan Kristi <steve.van.christie@gmail.com>

WORKDIR	/

RUN	apt update && \
	apt install -y npm nodejs-legacy && \
	npm list harp || npm install harp -g && \
	harp init site 

EXPOSE	9000

CMD harp server site
