from deepdiff import DeepDiff
from fastapi.testclient import TestClient

from duration_prediction_api import app

client = TestClient(app)


def test_prediction():
    test_ride = {
        'start_station_id': '31206',
        'rideable_type': 'docked_bike',
        'member_casual': 'casual',
        'started_at': '2020-04-06 07:54:59',
    }
    expected_response = {"duration": 23.46}
    actual_response = client.post("/predict", json=test_ride)
    print(actual_response.json())
    assert actual_response.status_code == 200
    diff = DeepDiff(
        actual_response.json(), expected_response, significant_digits=2
    )
    assert not diff
