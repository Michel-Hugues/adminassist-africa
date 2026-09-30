from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import engine, Base
from database import SessionLocal
import models


Base.metadata.create_all(bind=engine)

# Open a session, "lends" it to the road that needs it,
# and then automatically closes it afterward, whether the request succeeded or failed.
def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
def show_item(item: Item, db: Session = Depends(get_db)):
    db_item =  models.Item(name=item.name, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item) 

    return {"db_item": db_item}

