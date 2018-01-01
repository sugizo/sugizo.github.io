#!/bin/sh

start=$(date +%s)

# Install Package
mkdir -p ~/project/js/hexo
cd ~/project/js/hexo
#npm install hexo-cli

# Initalize Blog
#./node_modules/.bin/hexo init stifix

# install app
rm -rf ~/project/js/hexo/stifix/*
rsync -zavr ~/Cloud/MEGA/Git/hexo/stifix/ ~/project/js/hexo/stifix/

# Install Blog
cd stifix
npm install

# Create New Post
#./node_modules/.bin/hexo new "post"

# Run Server
./node_modules/.bin/hexo server
#npm start

# Access via Browser
open http://localhost:4000

# Generate Static Site
./node_modules/.bin/hexo generate
#npm generate

# check public folder change external js and css into internal (save) then concat and minify it

end=$(date +%s)
diff=$(( $end - $start ))

echo Duration = $diff Seconds
echo Finished at = `date +%Y-%m-%d\ %H:%M:%S`
