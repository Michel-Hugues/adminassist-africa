from pydantic import BaseModel


# A class Item that inherits from BaseModel
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