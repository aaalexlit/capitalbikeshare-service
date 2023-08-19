FROM python:3.10-slim

RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app

COPY Pipfile* ./

RUN pipenv install --system --deploy

COPY src/* /app/src/

EXPOSE 8080

CMD ["uvicorn", "src.duration_prediction_api:app", "--host", "0.0.0.0", "--port", "80"]
