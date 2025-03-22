#!/bin/bash

sudo docker stop AmPayDB
sudo docker stop AmPayCache
sudo docker stop AmPayQueue

sudo systemctl stop docker.socket docker.service

echo "containers and docker stoped"