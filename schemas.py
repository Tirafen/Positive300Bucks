from typing import List, Optional
from pydantic import BaseModel, UUID4


class OrderBase(BaseModel):
    title: str
    description: Optional[str] = None


class OrderCreate(BaseModel):
    coffee_type: str


class Order(BaseModel):
    owner_id: UUID4
    coffee_type: str
    order_number: int
    ready = bool
    wait = bool
    in_progress = bool

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    name: str


class User(UserBase):
    orders: List[Order] = []

    class Config:
        orm_mode = True
