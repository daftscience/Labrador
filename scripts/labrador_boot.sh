#!/bin/bash

# sudo update-rc.d /etc/init.d/labrador_boot.sh defaults

su pi
cd /home/pi/projects/labrador
git pull

sudo supervisorctl stop labrador
sudo supervisorctl start labrador
