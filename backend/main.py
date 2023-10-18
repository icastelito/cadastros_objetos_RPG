from typing import Optional
from pydantic import BaseModel
import json
from fastapi import FastAPI, HTTPException
from typing import List
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
]



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    id: int
    name: str
    description: str
    rarity: Optional[str] = None
    type: Optional[str] = None
    power_category: int = None

# Carrega os dados do arquivo JSON
with open("data.json", "r") as json_file:
    items = json.load(json_file)

@app.get("/items/", response_model=List[Item])
def read_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item.dict())
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for item in items:
        if item["id"] == item_id:
            item.update(updated_item.dict())
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    global items
    updated_items = [item for item in items if item["id"] != item_id]
    if len(updated_items) == len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    items = updated_items
    return {"message": "Item deleted successfully"}
