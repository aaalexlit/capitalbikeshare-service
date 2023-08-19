from pydantic import BaseModel
from pydantic.config import ConfigDict

from src.utils import load_test_ride


class PredictionOutput(BaseModel):
    duration: float


class RideInput(BaseModel):
    start_station_id: str
    end_station_id: str
    rideable_type: str
    member_casual: str
    started_at: str

    model_config = ConfigDict(json_schema_extra={"example": load_test_ride()})
