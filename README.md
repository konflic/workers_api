# Database of workers

Application is made for managing workers.

## Requirements

- Python 3.7+
- Docker
- Docker-compose

## Setup with docker-compose

Application can be started with docker-compose. 
Before launching adjust environment variables in ```.env.example``` file according to your needs and rename it to ```.env```.
Below command will launch application according to current configuration in detached mode.

```
docker-compose up -d
```

Use command to stop application

```
docker-compose down
```

## Setup locally

In order to setup and run application locally

0. Setup virtual environment

```
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requiremetns.txt
```

After this make sure you use only venv environment.

1. Setup container with database using python script

```
python tests/setup_pg_container.py
```

2. Run application

```
python main.py
```

## Tests

In order to run tests against application.
Make sure you use correct configuration for test run.

```
PYTHONPATH=$(pwd) pytest
```
