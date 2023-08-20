from src.utils import load_test_ride
from src.schemas import RideInput
from src.duration_prediction_api import prepare_features


def test_prepare_features():
    test_ride = RideInput.model_validate(load_test_ride())
    features = prepare_features(test_ride)
    assert features == {
        "start_station_id": "31205",
        "end_station_id": "31239",
        "rideable_type": "docked_bike",
        "member_casual": "member",
        "month": 4,
        "hour": 7,
        "year": 2020,
    }
