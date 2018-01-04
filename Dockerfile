FROM node

#LABEL stifix

COPY . /site/

WORKDIR /site

RUN npm install

EXPOSE 1111

CMD /site/node_modules/.bin/roots watch
