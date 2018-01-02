FROM node

#LABEL stifix

RUN groupadd -r nodejs && \
 useradd -m -r -g nodejs nodejs

USER nodejs

RUN npm list harp || npm install harp

COPY . /home/nodejs/site/
WORKDIR /home/nodejs/site/

EXPOSE 9000

CMD /home/nodejs/site/node_modules/.bin/harp server site
