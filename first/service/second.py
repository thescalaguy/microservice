import requests
import os

from common.zookeeper import get_service_from_zookeeper


def make_request() -> dict:
    service = get_service_from_zookeeper(service="second")
    url = f"http://{service.host}:{service.port}"
    response = requests.post(url)
    response.raise_for_status()
    return response.json()
