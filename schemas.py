from pydantic import BaseModel
from pydantic.config import ConfigDict


class PredictionOutput(BaseModel):
    duration: float


class RideInput(BaseModel):
    start_station_id: str
    rideable_type: str
    member_casual: str
    started_at: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                'start_station_id': '31205',
                'rideable_type': 'docked_bike',
                'member_casual': 'member',
                'started_at': '2020-04-06 07:54:59',
            }
        }
    )
