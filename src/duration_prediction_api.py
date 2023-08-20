from pathlib import Path
from datetime import datetime

import wandb
import joblib
import uvicorn
from fastapi import FastAPI

from src.schemas import RideInput, PredictionOutput

BASE_DIR = Path(__file__).resolve(strict=True).parent

artifact = wandb.Api().artifact(
    "model-registry/capitalbikeshare-dv-model-pipeline:staging", type="model"
)
pipeline_path = Path(artifact.download(root=BASE_DIR)) / "pipeline.pkl"

with open(pipeline_path, 'rb') as f_out:
    pipeline = joblib.load(f_out)

app = FastAPI(
    title="Duration Prediction API",
    description="API to predict the duration of a cycling trip",
    version="1.0",
)


def prepare_features(ride: RideInput) -> dict:
    started_at = datetime.strptime(ride.started_at, "%Y-%m-%d %H:%M:%S")
    return {
        "start_station_id": ride.start_station_id,
        "end_station_id": ride.end_station_id,
        "rideable_type": ride.rideable_type,
        "member_casual": ride.member_casual,
        "hour": started_at.hour,
        "month": started_at.month,
        "year": started_at.year,
    }


@app.post("/predict", response_model=PredictionOutput)
def predict(ride: RideInput) -> PredictionOutput:
    features = prepare_features(ride)
    duration = pipeline.predict(features)[0]
    return {"duration": duration}


@app.get("/healthcheck")
def healthcheck() -> dict:
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("duration_prediction_api:app", reload=True)
