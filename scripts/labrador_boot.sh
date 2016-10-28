#!/bin/bash

# sudo systemctl enable /home/pi/projects/labrador/scripts/labrador.service
# sudo systemctl start labrador.service
cd /home/pi/projects/labrador
git pull

chmod +x /home/pi/projects/labrador/scripts/labrador_boot.sh
sudo supervisorctl stop labrador
sudo supervisorctl start labrador
