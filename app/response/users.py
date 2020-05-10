from pydantic import BaseModel


class UserCreateResponse(BaseModel):
    code: str = None
    # data: dict = {"Oauth-Token": str, "expire": 86400*7}
    data: dict
    msg: str = None

    class Config:
        orm_mode = True

class UserCurrentResponse(BaseModel):
    code: str = None
    # data: dict = {"nickname": str, "avatar": '', "id": int, "username": str}
    data: dict
    msg: str = None
