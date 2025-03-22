#!/bin/bash

sudo systemctl start docker.service

sudo docker start AmPayDB
sudo docker start AmPayCache
sudo docker start AmPayQueue

echo "containers are working"