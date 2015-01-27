# This is a shell script to automate the process of install py-gaugette. How to download and use this is all covered in 

sudo apt-get install git-core -y
sudo apt-get install python-setuptools -y
sudo apt-get install python-dev -y
sudo apt-get install python-imaging -y
git clone git://git.drogon.net/wiringPi
cd wiringPi
sudo ./build
git clone https://github.com/Gadgetoid/WiringPi2-Python.git
cd WiringPi2-Python/
sudo python setup.py install
./build.sh
cd ..
git clone https://github.com/doceme/py-spidev
cd py-spidev
sudo python setup.py install
cd ..
git clone https://github.com/guyc/py-gaugette.git
cd py-gaugette
sudo python setup.py install
cd
cd OLED/python-examples
wget http://lorempixel.com/output/people-q-c-128-64-1.jpg # This downloads a picture of a people face for one of the Python examples
cd
