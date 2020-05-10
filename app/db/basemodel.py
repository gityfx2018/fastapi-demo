from datetime import datetime

import orm

from .database import database, metadata


class BaseModel(orm.Model):
    __abstract__ = True

    id = orm.Integer(primary_key=True)
    created_at = orm.DateTime(allow_null=True, default=datetime.now())
    updated_at = orm.DateTime(allow_null=True)
