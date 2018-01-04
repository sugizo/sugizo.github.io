FROM python:2.7

#LABEL stifix

RUN pip install Cactus

EXPOSE 8000

COPY . /site/
WORKDIR /site

CMD cactus serve
