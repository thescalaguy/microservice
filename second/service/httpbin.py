import requests
import random


def make_request() -> dict:
    response = requests.post(f"https://httpbin.org/delay/0")
    response.raise_for_status()
    return response.json()
