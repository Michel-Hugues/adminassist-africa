from fastapi import FastAPI
from pydantic import BaseModel

# A basic API Instance
app = FastAPI()

# A class Item that inherits from BaseModel
class Item(BaseModel):
    name: str
    description : str = "A description for the item"
    price: float

    
# A GET / endpoint that returns a simple JSON message, such as {"message": "..."}
@app.get("/message")
def read_message():
    return {"message":"You can do it"}

# A second GET route /health that returns a status
@app.get("/health")
def status():
    return {"status": "OK"}

@app.post("/items")
def show_item(item: Item):
    return {"item": item}
