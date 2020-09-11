from typing import List, Optional

from lib.util import logger
from pydantic import BaseModel


def add(items: List[float]):
    if (a := items[0]) < 1:
        logger.warning("Oh no! {} < 1", a)

    s = sum(items)
    logger.success("Sum of {} = {}", items, s)
    return s


class Item(BaseModel):
    items: List[float]
    total: Optional[float] = None
