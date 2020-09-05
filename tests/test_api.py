from lib.util import ApiClient
from main import app

tester = ApiClient(app)


def test_root():
    response = tester.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_add():
    response = tester.post("/add", {"items": [-1, 2, 3]})
    assert response.status_code == 200
    assert response.json() == {"sum": 4}
