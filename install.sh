# Install Package
#mkdir -p ~/project/js/harp
#cd ~/project/js/harp
#npm list harp || npm install harp
mkdir -p ~/project/js/harp/stifix
cd ~/project/js/harp/stifix
npm list harp || npm install

# Initialize Site
#node_modules/.bin/harp init stifix

# install app
mkdir -p ~/project/js/harp/stifix/
rm -rf ~/project/js/harp/stifix/*
rsync -avuzr ~/Cloud/MEGA/Git/harp/stifix/* ~/project/js/harp/stifix/

# Run App
#cd ~/project/js/harp/
#./node_modules/.bin/harp server stifix
cd ~/project/js/harp/stifix
./node_modules/.bin/harp server 

# Check App on Browser
#http://localhost:9000

# Compile App
#cd ~/project/js/harp/
#./node_modules/.bin/harp compile stifix
cd ~/project/js/harp/stifix
./node_modules/.bin/harp compile 

# Check generated files
du -hsc ~/project/js/harp/stifix/www/
