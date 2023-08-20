#!/usr/bin/env bash

echo "Starting integration test"

# cd to the directory where the script is
# if it's not a github action execution
if [[ -z "${GITHUB_ACTIONS}" ]]; then
  echo "Switching to the script directory: $(dirname "$0")"
  cd "$(dirname "$0")"
fi

cd ..

echo "Building and running docker container"
docker compose up --build -d

echo "Waiting for the service to spin up"
sleep 30

echo "Calling dockerized service"
pipenv run python -m pytest integration-test/test_docker.py

ERROR_CODE=$?

if [ ${ERROR_CODE} != 0 ]; then
    docker compose logs
    docker compose down
    exit ${ERROR_CODE}
fi

echo "removing docker container"
docker compose down
