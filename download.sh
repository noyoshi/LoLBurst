#!/bin/bash 

pip3 install -r requirements.txt
chmod +x download.py
./download.py
unzip champ_info.zip 
make
chmod +x testme.sh
