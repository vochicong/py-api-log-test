from typing import List

from loguru import logger
from pydantic import BaseModel

from lib.util import set_logger

set_logger(logger)


def add(items: List[float]):
    if (a := items[0]) < 1:
        logger.warning("Oh no! {} < 1", a)

    s = sum(items)
    return s


class Item(BaseModel):
    items: List[float]
