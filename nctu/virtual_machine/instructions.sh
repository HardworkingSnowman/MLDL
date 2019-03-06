#!/bin/bash

# install python3
sudo apt-get update
sudo apt-get install -y python3

# install & upgrade pip
sudo apt-get install -y python3-pip python3-dev build-essential
python3 -m pip install --upgrade pip
pip3 install --user -U setuptools

# install python3 packages
pip3 install --user scikit-learn numpy pandas openpyxl beautifulsoup4 matplotlib tensorflow keras python-docx PyPDF2

# install jupyter lab
pip3 install --user jupyterlab
jupyter notebook --generate-config

openssl req -x509 -newkey rsa:4096\
            -keyout /home/ubuntu/.ssh/mycert.key\
            -out /home/ubuntu/.ssh/mycert.pem\
            -days 365 -nodes\
            -subj '/C=US/ST=Oregon/L=Portland/O=Company Name/OU=Org/CN=www.example.com'\

cat jupyter_setting.txt >> ~/.jupyter/jupyter_notebook_config.py

echo '請輸入 jupyter lab 密碼兩次（恩 螢幕不會出現你的密碼，是正常ㄉ）：'
jupyter notebook password
