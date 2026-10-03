from sqlalchemy import Column, Integer , String, Float
from database import Base

class Item(Base):
    __tablename__ = "items"
    id   = Column(Integer,primary_key=True, index=True)
    name = Column(String) 
    description = Column(String)
    price = Column(Float)

class User(Base):
    __tablename__ = "users"
    id   = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True) 
    hashed_password = Column(String)
