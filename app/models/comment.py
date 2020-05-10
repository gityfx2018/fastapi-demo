import orm

from app.models.users import User
from app.db.database import database, metadata
from app.db.basemodel import BaseModel
from app.models.article import Articles


class Comment(BaseModel):
    __tablename__ = "comment"
    __database__ = database
    __metadata__ = metadata

    user_id = orm.ForeignKey(
        User,
        allow_null=True
    )
    article_id = orm.ForeignKey(
        Articles,
        allow_null=True
    )
    content = orm.String(
        max_length=255,
        allow_null=True
    )
    parent_id = orm.Integer(allow_null=True)
    to_uid = orm.Integer(allow_null=True)
    level_flag = orm.String(allow_null=True, max_length=255)
