#!/usr/bin/env bash

# cd to the directory where the script is if it's not a github action execution
if [[ -z "${GITHUB_ACTIONS}" ]]; then
  cd "$(dirname "$0")"
fi

cd ..

source ../.env set

docker compose up --build -d

sleep 30

pipenv run pytest integration-test/test_docker.py

ERROR_CODE=$?

if [ ${ERROR_CODE} != 0 ]; then
    docker compose logs
    docker compose down
    exit ${ERROR_CODE}
fi

docker compose down
