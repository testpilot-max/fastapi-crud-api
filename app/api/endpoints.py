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

@router.get("/items/search")
def search_items(query: str):
    # Violates the 'no-print-statements' rule
    print(f"Searching for: {query}")
    # Implementation omitted
    return {"message": "Search functionality not implemented"}

@router.put("/items/{item_id}")
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    # Violates the 'proper-exception-handling' rule
    try:
        db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        for key, value in item.dict().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
        return db_item
    except:
        # Bare except clause
        print("An error occurred")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    # Violates the 'consistent-return-annotation' rule (no return type annotation)
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

@router.get("/items/stats")
async def get_item_stats(db: Session = Depends(database.get_db)) -> Any:
    # Violates multiple rules: 'no-print-statements' and 'proper-exception-handling'
    try:
        total_items = db.query(models.Item).count()
        print(f"Total items: {total_items}")  # Print statement
        avg_price = db.query(func.avg(models.Item.price)).scalar()
        return {"total_items": total_items, "average_price": avg_price}
    except:
        # Bare except clause
        print("Error calculating stats")
        return {"error": "Could not calculate stats"}