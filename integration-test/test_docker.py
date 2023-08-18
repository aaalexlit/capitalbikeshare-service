import httpx
from deepdiff import DeepDiff

test_ride = {
    'start_station_id': '31205',
    'rideable_type': 'docked_bike',
    'member_casual': 'member',
    'started_at': '2020-04-06 07:54:59',
}


def test_service():
    url = "http://127.0.0.1/predict"
    expected_response = {"duration": 12.88}
    actual_response = httpx.post(url, json=test_ride)
    assert actual_response.status_code == 200
    diff = DeepDiff(
        actual_response.json(), expected_response, significant_digits=2
    )
    assert not diff


if __name__ == "__main__":
    test_service()
