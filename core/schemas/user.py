from datetime import date
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    first_name : str
    last_name : str
    password : str
    age : int
    weight : float
    height : float


class User(BaseModel):
    id: int
    email: str
    first_name : str
    last_name : str
    age : int
    weight : float
    height : float

    class Config:
        orm_mode=True


class UserLogin(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    first_name : str
    last_name : str
    age : int
    weight : float
    height : float