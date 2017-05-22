# SimpleDjangoApp
project available on dockerhub at jedra/simpledjangoapp
## Instructions
- ```$git clone https://github.com/JedraPeake/SimpleDjangoApp.git```
- ```cd simpledjangoapp```

#### Setting up the docker machine
- ```$docker-machine create -d virtualbox dev;```
- ```$eval $(docker-machine env dev)```
- ```$docker-machine ls```

#### Docker Compose
- ```$docker-compose build```
- ```$docker-compose up -d```
- ```$docker-compose run web python manage.py migrate```

#### Grab IP
- ```$docker-machine ip dev```
