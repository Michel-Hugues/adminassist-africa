from fastapi import FastAPI, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
import schemas
from database import engine, Base
from database import SessionLocal
import models
import auth

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

@app.post("/register", response_model = schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_pw = auth.hash_password(user.password)
    db_user =  models.User(email=user.email, hashed_password = hashed_pw)
    db.add(db_user)
    db.commit()         # I pass this db_item (SQLAlchemy) to the session
    db.refresh(db_user) # The session translates this into actual SQL and sends it to test.db

    return db_user

@app.post("/login")
def login(user:  schemas.UserCreate, db: Session = Depends(get_db)):
    db_user =  db.query(models.User).filter(models.User.email == user.email).first()
    
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = auth.create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}