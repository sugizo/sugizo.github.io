FROM ubuntu:latest

#MAINTAINER Stifan Kristi <steve.van.christie@gmail.com>

RUN apt update && \
	apt install -y python python-pip python-setuptools unzip vim wget gunicorn && \
	pip install --upgrade pip && \
	pip install virtualenv && \
	virtualenv /home/site && \
	rm -rf /home/site/web2py && \
	cd /home/site/ && \
	rm -f web2py_src.zip && \
	wget -c http://web2py.com/examples/static/web2py_src.zip && \
	unzip -o web2py_src.zip && \
	rm -rf /home/site/web2py/applications/examples && \
	chmod 755 -R /home/site/web2py

EXPOSE 80 

COPY start.sh /start.sh

RUN chmod 755 /start.sh

CMD ["./start.sh"]
