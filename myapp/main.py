from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="kmtake test API")


class Item(BaseModel):
    id: int
    name: str
    description: str | None = None


_store: dict[int, Item] = {}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = _store.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    if item.id in _store:
        raise HTTPException(status_code=400, detail="Item already exists")
    _store[item.id] = item
    return item
