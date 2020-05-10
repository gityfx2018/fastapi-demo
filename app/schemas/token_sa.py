from pydantic import BaseModel


class TokenBase(BaseModel):
    pass


class Token(TokenBase):
    token: str
    token_type: str
