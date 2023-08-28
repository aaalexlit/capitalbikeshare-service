import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


def load_test_ride():
    with open(
        Path(__file__).parent / "test_ride.json", "rt", encoding="utf-8"
    ) as f_in:
        return json.load(f_in)
