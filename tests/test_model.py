from loguru_caplog import loguru_caplog as caplog
from lib.model import add


def test_add(caplog):
    assert add([-1, 3]) == 2
    assert "Oh no" in caplog.text
