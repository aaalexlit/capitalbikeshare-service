import wandb
import uvicorn
from fastapi import FastAPI

artifact = wandb.Api().artifact(
    "model-registry/capitalbikeshare-dv-model-pipeline:staging", type="model"
)

app = FastAPI(
    title="Duration Prediction API",
    description="API to predict the duration of a trip",
    version="1.0",
)


@app.post("/predict")
def predict() -> dict:
    return {"duration": 100}


@app.get("/healthcheck")
def healthcheck() -> dict:
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("duration_prediction_api:app", reload=True)
