[![Codacy Badge](https://api.codacy.com/project/badge/Grade/16738458af0643f9a3ec8bec7a634dcb)](https://www.codacy.com/manual/kryvokhyzha/basic-docker-container-for-ds?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kryvokhyzha/basic-docker-container-for-ds&amp;utm_campaign=Badge_Grade)

# basic-docker-container-for-ds

## About
This is template for creating Data Science project.

## Run project
1.  Clone this repo

Create a new folder with project name, cd into it, and then run:

```bash
$ git init
$ git pull https://github.com/kryvokhyzha/basic-docker-container-for-ds.git
```

2.  Add your favorite Python modules to _./docker/jupyter/requirements.txt_
For example:

```bash
statsmodels
torch==1.3
```

3.  Change image name in _docker-compose_ file:
```yaml
    image: docker_user/app_name:tag
```

4.  Run containers:

```bash
$ docker-compose up
```
or
```bash
$ docker-compose up --build
```

5.  Copy a jupyter url from terminal and open it in your browser
6.  Create your notebook in _notebooks_ folder
7.  Copy your data into _./data_ and read it in Jupyter. You also can upload data into PostgresSQL, which is running in it's own container along with Jupyter
8.  Close terminal to stop running jupyter and postgres
9.  Stop containers and removes containers, networks, volumes, and images:

```bash
$ docker-compose down
```

10. Clean Docker's mess:

```bash
$ docker rmi -f $(docker images -qf dangling=true)
```

Sometimes it is useful to remove all docker's data:

```bash
$ docker system prune
```

## Disable PostgreSQL server
1.  Go to the file _docker-complose.yml_
2.  Delete _volumes_ section under _db_

```yaml
volumes: 
    pgdata:
```

3.  Delete whole _db_ section 

Now, _docker-compose.yml_ looks like:
```yaml
version: '3'
services: 
    jupyter:
        build: 
            context: ./docker/jupyter/
            dockerfile: Dockerfile
        docker_user/app_name:tag
        volumes: 
            - .:/home/jovyan/
        ports: 
            - "8888:8888"
        environment: 
            - JUPYTER_ENABLE_LAB=yes
```

5.  Delete _./docker/postgres/_ folder
4.  Run project (see previous paragraph)

## Usefull commnads

### Show running containers
```bash
$ docker ps
```

### Show all containers
```bash
$ docker ps --all
```

### Show all top level images
```bash
$ docker images
```

### Build container
```bash
$ docker -t build <tag-name> .
```
_this command works, when Dockerfile is placed in current directory_

### Run container with volume
```bash
$ docker run --rm -p <local-port>:<docker-port> -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/ <tag-name>
```
_PWD_ - prints the path of the working directory, starting from the root

### Create volume for postgresql
```bash
$ docker volume create pgdata
```

_pgdata_ - is volume name for postgresql

### Docker compose up
```bash
$ docker-compose up
```

### Docker compose up with build
```bash
$ docker-compose up --build
```

### Docker compose down
```bash
$ docker-compose down
```

### Attach to running container
```bash
$ docker exec -it <mycontainerID> bash
```

### Copy file into the running container
```bash
$ docker cp <data-filename> <mycontainerID>:/home/jovyan/<data-filename>
```
