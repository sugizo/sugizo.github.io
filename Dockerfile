FROM node

#LABEL stifix

RUN groupadd -r nodejs && \
 useradd -m -r -g nodejs nodejs

USER nodejs

COPY . /home/nodejs/site/

RUN mkdir -p /home/nodejs/site && \
 cd /home/nodejs/site && \
 npm install

EXPOSE 1111

CMD cd /home/nodejs/site/node_modules/.bin/roots watch
