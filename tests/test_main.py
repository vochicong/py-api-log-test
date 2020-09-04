from lib.util import Tester
from main import app

tester = Tester(app)


def test_read_main():
    response = tester.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_add_item():
    response = tester.post("/add", {"items": [-1, 2, 3]})
    assert response.status_code == 200
    assert response.json() == {"sum": 4}
