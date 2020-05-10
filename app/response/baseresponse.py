from pydantic import BaseModel


class BaseModelResponse(BaseModel):
    code: str = "200"
    msg: str = "success"
    data: dict