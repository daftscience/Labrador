#!/bin/bash

# sudo systemctl enable /home/pi/projects/labrador/scripts/labrador.service
# sudo systemctl start labrador.service
cd /home/pi/projects/labrador
git pull

sudo supervisorctl stop labrador
sudo supervisorctl start labrador
