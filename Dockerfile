FROM python:3.10-slim

ARG WANDB_API_KEY

RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app

COPY Pipfile* ./

RUN pipenv install --system --deploy

COPY src/*.py src/
COPY src/*.json src/

RUN export PYTHONPATH="${PYTHONPATH}:$(pwd)" && \
    python src/download_model.py $WANDB_API_KEY

EXPOSE 8080

CMD ["uvicorn", "src.duration_prediction_api:app", "--host", "0.0.0.0", "--port", "80"]
