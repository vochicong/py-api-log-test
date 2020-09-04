import sys

from fastapi import FastAPI
from loguru import logger

from lib.model import Item, add
from lib.util import set_logger

set_logger(logger)
app = FastAPI()


@app.get("/")
async def read_main():
    logger.debug("Hello")
    logger.info("Hello")
    return {"msg": "Hello World"}


@app.post("/add")
def add_item(item: Item):
    s = add(item.items)
    logger.success("Sum = {}", s)
    return {"sum": s}
