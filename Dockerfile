FROM python:3.10-slim

RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app

COPY Pipfile* ./

RUN pipenv install --system --deploy

COPY duration_prediction_api.py ./
COPY schemas.py ./

EXPOSE 8080

CMD ["uvicorn", "duration_prediction_api:app", "--host", "0.0.0.0", "--port", "80"]
