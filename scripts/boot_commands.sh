#!/bin/bash

cd /home/pi/projects/labrador
git pull

sudo supervisorctl stop labrador
sudo supervisorctl start labrador
