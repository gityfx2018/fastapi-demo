from datetime import timedelta, datetime

import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.api.operation.users import get_user_by_username
from app.services.jwt import verify_password, SECRET_KEY, ALGORITHM


async def authenticate_user(username: str, password: str):
    user = await get_user_by_username(username=username)
    if not user:
        return False
    if not verify_password(password, user[0].password):
        return False
    return user


def create_access_token(*, data: dict, expire_time: timedelta = None):
    to_encode = data.copy()
    if expire_time:
        expire = expire_time + datetime.utcnow()
    else:
        expire = datetime.utcnow() + timedelta(days=7)

    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return token
