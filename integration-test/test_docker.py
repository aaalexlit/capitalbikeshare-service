import httpx
from deepdiff import DeepDiff

from src.utils import load_test_ride


def test_service():
    url = "http://127.0.0.1/predict"
    expected_response = {"duration": 12.80}
    actual_response = httpx.post(url, json=load_test_ride(), timeout=30)
    assert actual_response.status_code == 200
    diff = DeepDiff(
        actual_response.json(), expected_response, exclude_paths='duration'
    )
    assert not diff


if __name__ == "__main__":
    test_service()
