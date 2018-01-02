FROM ruby

#LABEL stifix

RUN apt install -y nodejs-legacy && \
 gem install jekyll bundler jekyll-minifier jekyll-sitemap 

COPY . /site/

WORKDIR /site

EXPOSE 4000

CMD bundle exec jekyll serve --host 0.0.0.0
