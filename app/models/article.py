import orm

from app.db.basemodel import BaseModel
from app.db.database import database, metadata
from app.models.users import User


class Tags(BaseModel):
    __tablename__ = 'tags'
    __database__ = database
    __metadata__ = metadata

    name = orm.String(max_length=255, allow_null=True)
    avatar = orm.String(max_length=255, allow_null=True)

    def __str__(self):
        return self.name


class CateGory(BaseModel):
    __tablename__ = 'categorys'
    __database__ = database
    __metadata__ = metadata

    category_name = orm.String(max_length=255, allow_null=True)
    avatar = orm.String(max_length=255, allow_null=True)
    description = orm.String(max_length=255, allow_null=True)

    def __str__(self):
        return self.category_name


class Articles(BaseModel):
    __tablename__ = 'articles'
    __database__ = database
    __metadata__ = metadata

    title = orm.String(max_length=255, allow_null=True)
    summary = orm.String(max_length=255, allow_null=True)
    views = orm.Integer(default=0)
    comment_num = orm.Integer(default=0)
    weight = orm.Integer(default=0)
    content = orm.Text()  # txt
    content_html = orm.Text()  # html
    is_hot = orm.Boolean(default=False)
    key_words = orm.String(max_length=255, allow_null=True)
    tag_id = orm.ForeignKey(
        Tags,
        allow_null=True
    )

    user_id = orm.ForeignKey(
        User,
        allow_null=True
    )

    def __str__(self):
        return self.title


class ArticleTag(BaseModel):
    __tablename__ = 'articles_tags'
    __database__ = database
    __metadata__ = metadata

    article_id = orm.ForeignKey(
        Articles,
        allow_null=True
    )
    tag_id = orm.ForeignKey(
        Tags,
        allow_null=True
    )
