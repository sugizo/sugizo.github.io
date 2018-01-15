FROM node

#LABEL stifix

COPY . /site/
WORKDIR /site

RUN npm list wintersmith || npm install wintersmith -g

EXPOSE 8080

CMD wintersmith preview
