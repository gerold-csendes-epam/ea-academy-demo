#!/bin/bash
#Perform a quick update on your instance:
sudo yum update -y

#Install git in your EC2 instance
sudo yum install git -y

cd home
git clone https://github.com/gerold-csendes-epam/ea-academy-demo.git
cd ea-academy-demo

python3 -m venv streaming-demo
source streaming-demo/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt