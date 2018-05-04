#!/bin/bash

sudo apt-get update

sudo apt-get upgrade

curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

sudo apt install python3-pip
pip3 install tensorflow
pip3 install keras

git clone https://github.com/sachinmsundar/ccaProject.git
cd ccaProject

npm init

npm install express --save
npm install ejs --save

sudo npm install -g forever

sudo iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080
