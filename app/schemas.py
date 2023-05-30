from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class UserR(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
       orm_mode=True


class PostR(PostBase):
    id: int
    content: str
    created_at: datetime
    owner_id: int

    class Config:
       orm_mode=True

class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserR

    class Config:
       orm_mode=True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str]
    




class CreateUser(BaseModel):
    email: EmailStr
    password: str
  

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # Restricting value to 1 or 0 
    

class PostVote(BaseModel):
    Post: Post
    votes: int

    class Config:
       orm_mode=True