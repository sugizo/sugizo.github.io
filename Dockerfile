FROM composer

#LABEL stifix

COPY . /site/

RUN apk update && \
 apk --no-cache add python && \
 cd /site && \
 composer require tightenco/jigsaw && \
 ./vendor/bin/jigsaw build

EXPOSE 8000

WORKDIR /site/build_local

CMD python -m SimpleHTTPServer 8000
