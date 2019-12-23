# Build container
sudo docker -t build basic-ds .

# Run container with volume
sudo docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD"/src:/home/jovyan/work basic-ds

# Create volume for postgresql
sudo docker volume create pgdata

# Docker compose up
sudo docker-compose up

# Docker compose down
sudo docker-compose down

# Docker compose up with build
sudo docker-compose up --build

# Attach to running container
sudo docker exec -it <mycontainerID> bash

# Copy file into the running container
sudo docker cp wine.data <mycontainerID>:/home/jovyan/wine.data

