import json
import os
import sys
from urllib import response

import requests
from fastapi.testclient import TestClient

from lib.config import BASE_URL, DEBUG_LOG_FILE, LOG_LEVEL


class Tester:
    def __init__(self, app) -> None:
        if not BASE_URL:
            self.client = TestClient(app)

    def get(self, path):
        if BASE_URL:
            response = requests.get(BASE_URL + path)
        else:
            response = self.client.get(path)
        return response

    def post(self, path, data):
        if BASE_URL:
            response = requests.post(BASE_URL + path, data=json.dumps(data))
        else:
            response = self.client.post(path, json=data)
        return response


def set_logger(logger):
    logger.remove()
    logger.add(DEBUG_LOG_FILE, level="DEBUG", retention="10 days")
    logger.add(sys.stderr, level=LOG_LEVEL)
