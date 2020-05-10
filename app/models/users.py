import orm

from ..db.basemodel import BaseModel
from ..db.database import database, metadata


class User(BaseModel):
    __tablename__ = "user"
    __database__ = database
    __metadata__ = metadata

    username = orm.String(max_length=50)
    password = orm.String(max_length=255)
    email = orm.String(max_length=50, unique=True, index=True)
    phone = orm.String(allow_null=True, max_length=11)
    nickname = orm.String(allow_null=True, max_length=50)
    avatar = orm.String(allow_null=True, max_length=255)
    status = orm.String(allow_null=True, max_length=10)
    is_active = orm.Boolean(default=False)


    def __str__(self):
        return self.username


class ActivationCode(BaseModel):
    __tablename__ = "activatecode"
    __database__ = database
    __metadata__ = metadata

    code = orm.String(max_length=6, min_length=6, allow_null=True)
    user_id = orm.ForeignKey(
        User,
        allow_null=True
    )
