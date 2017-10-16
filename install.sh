#!/bin/sh

start=$(date +%s)

# Install Package
cd ~/Downloads/nodejs/learn
npm install hugo-cli

# Initalize Blog
rm -rf stifix
node_modules/.bin/hugo new site stifix

# install app
rsync -zavr ~/Cloud/Dropbox/Programming/JS/Hugo/stifix ~/Downloads/nodejs/learn/

# Add Theme
cd stifix/themes
git clone https://github.com/schmanat/hugo-highlights-theme

# Run Server
cd ..
../node_modules/.bin/hugo server -D

# Access Server via Browser
#http://localhost:1313

end=$(date +%s)
diff=$(( $end - $start ))

echo Duration = $diff Seconds
echo Finished at = `date +%Y-%m-%d\ %H:%M:%S`
