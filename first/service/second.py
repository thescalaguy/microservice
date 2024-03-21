import requests
import os


def make_request() -> dict:
    url = os.environ.get("SECOND", "http://localhost:6000")
    response = requests.post(url)
    response.raise_for_status()
    return response.json()
