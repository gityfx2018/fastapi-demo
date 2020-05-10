from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    avatar: str = None
    # email: EmailStr


class UserCreate(UserBase):
    nickname: str
    password: str


class UserActivated(UserBase):
    id: int
    is_active: bool
    email: EmailStr


class User(UserBase):
    id: int
    nickname: str

    class Config:
        orm_mode = True
