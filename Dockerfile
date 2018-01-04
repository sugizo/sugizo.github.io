FROM node

#LABEL stifix

COPY . /site/
WORKDIR /site

RUN npm list hexo-cli || npm install hexo-cli -g && \
 npm install

EXPOSE 4000

CMD hexo server
