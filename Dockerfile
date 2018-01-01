FROM ubuntu:latest

#MAINTAINER Stifan Kristi <steve.van.christie@gmail.com>

COPY . /site/
WORKDIR	/

RUN	apt update && \
	apt install -y npm nodejs-legacy && \
	npm list hugo-cli || npm install hugo-cli -g

EXPOSE	1313

CMD cd site && hugo server --bind 0.0.0.0 -D
