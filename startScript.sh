#!/bin/bash

sudo apt-get update

sudo apt-get upgrade

curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

mkdir ccaProject
cd ccaProject

npm init

npm install express --save
npm install ejs --save
