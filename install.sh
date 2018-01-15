# Install Package
mkdir -p ~/project/coffee/wintersmith
cd ~/project/coffee/wintersmith
npm list wintersmith || npm install wintersmith

# New Site
#./node_modules/.bin/wintersmith new stifix

# install app
mkdir -p ~/project/coffee/wintersmith/stifix/
rm -rf ~/project/coffee/wintersmith/stifix/*
rsync -avuzr ~/Cloud/MEGA/Git/wintersmith/stifix/* ~/project/coffee/wintersmith/stifix/

# Run App
cd stifix
../node_modules/.bin/wintersmith preview

# Check App on Browser
http://localhost:8080

# Compile App
../node_modules/.bin/wintersmith build

# Check generated files
du -hsc ~/project/coffee/wintersmith/stifix/build
