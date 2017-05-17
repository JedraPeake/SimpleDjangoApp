# SimpleDjangoApp

## Instructions

#### Setting up the docker machine
- Step 1. ```$docker-machine create -d virtualbox dev;```
- Step 2. ```$eval $(docker-machine env dev)```
- Step 3. ```$docker-machine ls```

#### Docker Compose
- Step 4. ```$docker-compose build```
- Step 5. ```$docker-compose up -d```
- Step 6. ```$docker-compose run web python manage.py migrate```

#### Grab IP
- Step 7. ```$docker-machine ip dev```
