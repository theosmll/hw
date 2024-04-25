from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    password: str

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float

class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_date: Optional[str]
    status: str
