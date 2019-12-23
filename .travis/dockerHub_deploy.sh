#!/bin/sh
docker login -u $DOCKER_USER -p $DOCKER_PASS
docker-compose build --pull
docker-compose push
docker logout
