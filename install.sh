# Install Package
mkdir -p ~/project/coffee/roots
cd ~/project/coffee/roots
npm list roots || npm install roots

# New Site
#node_modules/.bin/roots new stifix

# install app
mkdir -p ~/project/coffee/roots/stifix/
rm -rf ~/project/coffee/roots/stifix/*
rsync -avuzr ~/Cloud/MEGA/Git/roots/stifix/* ~/project/coffee/roots/stifix/

# Install Prerequisites
cd ~/project/coffee/roots/stifix
npm install

# Run App
cd ~/project/coffee/roots/stifix
../node_modules/.bin/roots watch
#npm start

# Check App on Browser
#open http://localhost:1111

# Compile App
cd ~/project/coffee/roots/stifix
../node_modules/.bin/roots compile
#npm compile

# Check generated files
du -hsc ~/project/coffee/roots/stifix/public/
