# Install Package on Virtual Environment
mkdir ~/project
cd ~/project
virtualenv --no-site-packages python
source python/bin/activate
pip list | grep Cactus || easy_install cactus

# Create Site
#cd ~/project
#source python/bin/activate
#cactus create ~/project/python/cactus/stifix

# Install App
rm -rf ~/project/python/cactus/stifix
mkdir -p ~/project/python/cactus/stifix
rsync -avzr ~/Cloud/MEGA/Git/cactus/stifix/0.1/* ~/project/python/cactus/stifix/

# Serve Site
cd ~/project
source python/bin/activate
cd ~/project/python/cactus/stifix
cactus serve

# Access via Browser
#http://localhost:8000

# Build
cd ~/project
source python/bin/activate
cd ~/project/python/cactus/stifix
cactus build

# Check generated files
du -hsc ~/project/python/cactus/stifix/.build/
