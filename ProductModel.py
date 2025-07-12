from pydantic import BaseModel
from bson import objectid 

class Product(BaseModel):
    name: str
    description : str
    price : float
    quantity : int

class ProductData(Product):
    _id : objectid