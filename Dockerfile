FROM node

#LABEL stifix

COPY . /site/
WORKDIR /

RUN npm list hugo-cli || npm install hugo-cli -g

EXPOSE 1313

CMD cd site && hugo server --bind 0.0.0.0 -D
