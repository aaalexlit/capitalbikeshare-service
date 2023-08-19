To successfully run the project you need to have `.env` file in the root directory with the following variables:
```
WANDB_API_KEY=your_wandb_api_key
```

## Local execution

To run the dockerized API locally execute:
```shell
make run
```

it will build and run the docker container with the project exposing the API on port 80.

To make a request to the API run:
```shell
curl -H "Content-Type: application/json" -d '{ "start_station_id": "31206", "end_station_id": "31206", "rideable_type": "docked_bike", "member_casual": "casual", "started_at": "2020-04-06 07:54:59"}' -X POST http://127.0.0.1/predict
```

To stop the running docker container run:
```shell
make stop
```

## Local development
Also, the conda environment created in the [main repo](https://github.com/aaalexlit/capitalbikeshare-mlops) needs to be activated (eg it has pipenv already installed and uses a proper python version):
```shell
conda activate capitalbikeshare-mlops
```

To install the project dependencies run:
```shell
make setup
```

To run the project tests run:
```shell
make integration_test
```
it will run both unit and integration tests.

To run only unit tests run:
```shell
make test
```

Makefile commands should work without activating the pipenv environment, but for the git hooks to work it's better to activate pipenv environment:
```shell
pipenv shell
```
