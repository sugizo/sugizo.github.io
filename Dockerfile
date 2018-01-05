FROM ruby

#LABEL stifix

RUN apt update && \
 apt install -y sudo curl && \
 curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - && \
 apt update && \
 apt install -y nodejs && \
 gem install jekyll bundler jekyll-minifier jekyll-sitemap 

COPY . /site/

WORKDIR /site

EXPOSE 4000

CMD bundle exec jekyll serve --host 0.0.0.0
