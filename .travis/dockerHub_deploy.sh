#!/bin/sh

if [ "$TRAVIS_BRANCH" = "master" ] && [ "$TRAVIS_PULL_REQUEST" = "false" ]; then
    docker login -u "$DOCKER_USER" -p "$DOCKER_PASS"
    docker-compose build --pull
    docker-compose push
    docker logout
else
    echo "Is not a master!"
fi
