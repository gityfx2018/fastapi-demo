from pydantic import BaseModel


class TagBase(BaseModel):
    pass


class TagCreate(TagBase):
    name: str
    avatar: str = None


class Tag(TagBase):
    id: int
    name: str
    avatar: str = None

    class Config:
        orm_mode = True
