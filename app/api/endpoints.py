from fastapi import APIRouter, HTTPException
from app import schemas
from typing import List

router = APIRouter()

items = []

@router.post("/items/", response_model=schemas.Item)
async def create_item(item: schemas.ItemCreate):
    new_item = item.dict()
    new_item["id"] = len(items) + 1
    items.append(new_item)
    return new_item

@router.get("/items/", response_model=List[schemas.Item])
async def read_items():
    return items

@router.get("/items/{item_id}", response_model=schemas.Item)
async def read_item(item_id: int):
    if item_id < 1 or item_id > len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id - 1]