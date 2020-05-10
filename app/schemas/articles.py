from typing import List

from pydantic import BaseModel


class ArticlesBase(BaseModel):
    title: str
    key_words: List[str] = []


class ArticlesCreate(ArticlesBase):
    tags: List[str] = []


class Articles(ArticlesBase):
    id: int
    tags: List[str] = []
    is_hot: bool = False
    user_id: int

    class Config:
        orm_mode = True


