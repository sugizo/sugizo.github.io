# Install Package
mkdir -p ~/project/js/harp
cd ~/project/js/harp
npm list harp || npm install harp

# Initialize Site
#node_modules/.bin/harp init stifix

# install app
mkdir -p ~/project/js/harp/stifix/
rm -rf ~/project/js/harp/stifix/*
rsync -avuzr ~/Cloud/MEGA/Git/harp/stifix/* ~/project/js/harp/stifix/

# Run App
cd ~/project/js/harp/
node_modules/.bin/harp server stifix

# Check App on Browser
#http://localhost:9000

# Compile App
cd ~/project/js/harp/
node_modules/.bin/harp compile stifix

# Check generated files
du -hsc ~/project/js/harp/stifix/www/
