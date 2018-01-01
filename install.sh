# Install Jigsaw via Composer
mkdir -p ~/project/php/jigsaw/stifix
cd ~/project/php/jigsaw/stifix
composer show | grep jigsaw || composer require tightenco/jigsaw
#composer install

# Initialize a new project in the current folder
#./vendor/bin/jigsaw init

# Install app
rm -rf ~/project/php/jigsaw/stifix/build_local/*
rm -rf ~/project/php/jigsaw/stifix/source/*
rsync -avzr ~/Cloud/MEGA/Git/jigsaw/stifix/* ~/project/php/jigsaw/stifix/

# Build site
cd ~/project/php/jigsaw/stifix
./vendor/bin/jigsaw build

# Check generated files
du -hsc ~/project/php/jigsaw/stifix/build_local/

# Run Web Server
cd ~/project/php/jigsaw/stifix/build_local
python -m SimpleHTTPServer 8000
