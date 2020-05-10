from pydantic import BaseModel


class CateGoryBase(BaseModel):
    category_name: str
    avatar: str = None
    description: str


class CateGoryCreate(CateGoryBase):
    pass


class CateGory(CateGoryBase):
    id: int

    class Config:
        orm_mode = True