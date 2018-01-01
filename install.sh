#!/bin/sh

start=$(date +%s)

# Install Package
mkdir -p ~/project/go/hugo
cd ~/project/go/hugo
npm list hugo-cli || npm install hugo-cli

# Initalize Blog
rm -rf ~/project/go/hugo/stifix
mkdir -p ~/project/go/hugo/stifix
#node_modules/.bin/hugo new site stifix

# install app
rm -rf ~/project/go/hugo/stifix/content/*
rm -rf ~/project/go/hugo/stifix/layouts/*
rm -rf ~/project/go/hugo/stifix/public/*
rm -rf ~/project/go/hugo/stifix/static/*
rsync -zavr ~/Cloud/MEGA/Git/hugo/stifix/ ~/project/go/hugo/stifix/

# Run Server
cd ~/project/go/hugo/stifix
../node_modules/.bin/hugo server -D

# Access Server via Browser
#http://localhost:1313

# Generate Static Site Website on folder public
cd ~/project/go/hugo/stifix
../node_modules/.bin/hugo

# Check generated files
du -hsc ~/project/go/hugo/stifix/public/

# check public folder change external js and css into internal (save) then concat and minify it

end=$(date +%s)
diff=$(( $end - $start ))

echo Duration = $diff Seconds
echo Finished at = `date +%Y-%m-%d\ %H:%M:%S`
