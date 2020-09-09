from typing import List

from lib.util import logger
from pydantic import BaseModel


def add(items: List[float]):
    if (a := items[0]) < 1:
        logger.warning("Oh no! {} < 1", a)

    s = sum(items)
    return s


class Item(BaseModel):
    items: List[float]
