from deepdiff import DeepDiff
from fastapi.testclient import TestClient

from src.duration_prediction_api import app

client = TestClient(app)


def test_healthcheck():
    expected_response = {"status": "ok"}
    actual_response = client.get("/healthcheck")
    print(actual_response.json())
    assert actual_response.status_code == 200
    diff = DeepDiff(actual_response.json(), expected_response)
    assert not diff
