from lib.util import ApiClient, logger
from main import app

tester = ApiClient(app)


def test_root():
    response = tester.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_add():
    response = tester.post("/add", {"items": [-1, 2, 3]})

    logger.debug(response.status_code)
    assert response.status_code == 200

    logger.debug(response.json())
    assert response.json()["total"] == 4


def test_get_add():
    response = tester.get("/add?a=-1&b=2")

    logger.debug(response.status_code)
    assert response.status_code == 200

    logger.debug(response.json())
    assert response.json()["total"] == 1
