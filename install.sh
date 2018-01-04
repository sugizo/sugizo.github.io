#!/bin/sh

start=$(date +%s)

# Install Package
source ~/.rvm/scripts/rvm
gem install jekyll bundler jekyll-minifier jekyll-sitemap

# Create New Site
mkdir -p ~/project/ruby/jekyll/stifix
cd ~/project/ruby/jekyll/stifix

# install app
rm -f ~/project/ruby/jekyll/stifix/*
rsync -zavr ~/Cloud/MEGA/Git/jekyll/stifix/ ~/project/ruby/jekyll/stifix/

# Serve Site
source ~/.rvm/scripts/rvm
cd ~/project/ruby/jekyll/stifix
bundle exec jekyll serve --host 0.0.0.0

# Access Server via Browser
#http://localhost:4000

# Generated Static Site is on _site folder
source ~/.rvm/scripts/rvm
cd ~/project/ruby/jekyll/stifix
jekyll build

# Check generated files
du -hsc ~/project/ruby/jekyll/stifix/_site/

# check public folder change external js and css into internal (save) then concat and minify it

end=$(date +%s)
diff=$(( $end - $start ))

echo Duration = $diff Seconds
echo Finished at = `date +%Y-%m-%d\ %H:%M:%S`
