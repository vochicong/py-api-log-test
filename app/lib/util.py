import json
import sys

import requests
from fastapi.testclient import TestClient
from loguru import logger

from lib.config import BASE_URL, DEBUG_LOG_FILE, LOG_LEVEL

logger.remove()
logger.add(DEBUG_LOG_FILE, level="DEBUG", retention="10 days")
logger.add(sys.stderr, level=LOG_LEVEL)


class ApiClient:
    def __init__(self, app) -> None:
        if not BASE_URL:
            self.client = TestClient(app)

    def get(self, path):
        if BASE_URL:
            resp = requests.get(BASE_URL + path)
        else:
            resp = self.client.get(path)
        return resp

    def post(self, path, data):
        if BASE_URL:
            resp = requests.post(BASE_URL + path, data=json.dumps(data))
        else:
            resp = self.client.post(path, json=data)
        return resp
