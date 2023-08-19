include .env

test:
	export PYTHONPATH="${PYTHONPATH}:$(shell pwd)"
	pipenv run python -m pytest tests/

integration_test: test
	./integration-test/test.sh

quality_checks:
	pipenv run python -m isort .
	pipenv run python -m black .
	pipenv run python -m pylint --recursive=y .

setup:
	pipenv install --dev
	pre-commit install

run:
	docker compose up --build -d

stop:
	docker compose down
