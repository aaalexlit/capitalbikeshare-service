from deepdiff import DeepDiff
from fastapi.testclient import TestClient

from src.utils import load_test_ride
from src.duration_prediction_api import app

client = TestClient(app)


def test_prediction():
    expected_response = {"duration": 12.88}
    actual_response = client.post("/predict", json=load_test_ride())
    print(actual_response.json())
    assert actual_response.status_code == 200
    diff = DeepDiff(
        actual_response.json(), expected_response, significant_digits=2
    )
    assert not diff
