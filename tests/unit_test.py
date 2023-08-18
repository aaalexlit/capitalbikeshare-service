from schemas import RideInput
from duration_prediction_api import prepare_features


def test_prepare_features():
    test_ride = RideInput.model_validate(
        {
            "start_station_id": "31239",
            "rideable_type": "docked_bike",
            "member_casual": "casual",
            "started_at": "2020-04-06 07:54:59",
        }
    )
    features = prepare_features(test_ride)
    assert features == {
        "start_station_id": "31239",
        "rideable_type": "docked_bike",
        "member_casual": "casual",
        "hour": 7,
        "year": 2020,
    }
