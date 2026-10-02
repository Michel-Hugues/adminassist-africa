from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import schemas
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

# A GET / endpoint that returns a simple JSON message, such as {"message": "..."}
@app.get("/message")
def read_message():
    return {"message":"You can do it"}

# A second GET route /health that returns a status
@app.get("/health")
def status():
    return {"status": "OK"}

@app.post("/items" , response_model = schemas.ItemResponse)
def show_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item =  models.Item(name=item.name, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()         # I pass this db_item (SQLAlchemy) to the session
    db.refresh(db_item) # The session translates this into actual SQL and sends it to test.db

    return db_item

