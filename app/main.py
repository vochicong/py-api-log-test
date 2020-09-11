from fastapi import FastAPI
from lib.model import Item, add
from lib.util import logger

app = FastAPI()


@app.get("/")
async def read_main():
    logger.debug("Hello")
    logger.info("Hello")
    return {"msg": "Hello World"}


@app.post("/add", response_model=Item)
def add_item(item: Item):
    logger.debug("input {}", item)
    item.total = add(item.items)
    return item


@app.get("/add", response_model=Item)
def get_add(a: float, b: float):
    logger.debug("input {} + {}", a, b)
    item = Item(items=[a, b])
    return add_item(item)
