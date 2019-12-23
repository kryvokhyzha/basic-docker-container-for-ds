#!/bin/sh
echo "Start"
if [ "$TRAVIS_BRANCH" = "master" ] && ["$TRAVIS_PULL_REQUEST" = "false"]; then
    echo "In if"
    TAG="latest"
    echo "After TAG"
    
    docker login -u $DOCKER_USER -p $DOCKER_PASS
    docker-compose build --pull
    docker-compose push
    echo "After push"
    docker logout
else
echo "In else"
    TAG="$TRAVIS_BRANCH"
fi
echo "Finish"
