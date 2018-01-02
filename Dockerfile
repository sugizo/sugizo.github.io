FROM python:2.7

#LABEL stifix

RUN apt update && \
 apt install -y unzip wget

RUN groupadd -r web2py && \
 useradd -m -r -g web2py web2py

USER web2py

RUN cd /home/web2py/ && \
 wget -c http://web2py.com/examples/static/web2py_src.zip && \
 unzip -o web2py_src.zip && \
 rm -rf /home/web2py/web2py/applications/examples && \
 mv /home/web2py/web2py/applications/welcome /home/web2py/web2py/applications/init && \
 chmod 755 -R /home/web2py/web2py

COPY . /home/web2py/web2py/applications/init/

EXPOSE 8000

CMD cd ~ && python /home/web2py/web2py/web2py.py --nogui --no-banner -a 'a' -i 0.0.0.0 -p 8000
