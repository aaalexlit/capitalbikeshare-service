import httpx

test_ride = {
    "start_station_id": "31239",
    "rideable_type": "docked_bike",
    "member_casual": "casual",
    "hour": 17,
    "year": 2020,
}


def test_service():
    url = "http://127.0.0.1:8000/predict"
    response = httpx.post(url, json=test_ride)
    assert response.json() == {"duration": 100}
