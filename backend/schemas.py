from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    description : str = "A description for the item"
    price: float

class ItemResponse(BaseModel):
    id : int
    name: str
    description : str = "A description for the item"
    price: float

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: str
    password : str

class UserResponse(BaseModel):
    id : int
    email: str

    class Config:
        from_attributes = True