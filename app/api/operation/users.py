import random

import jwt
# from jwt import PyJWTError
from fastapi import Depends
from starlette.responses import JSONResponse
from fastapi.exceptions import HTTPException

from app.schemas import user
from app.models.users import User, ActivationCode
from app.services.jwt import hash_password, oauth2_scheme, SECRET_KEY, ALGORITHM


async def create_user(user_obj: user.UserCreate):
    user = await User.objects.create(username=user_obj.username, nickname=user_obj.nickname,
                                     password=hash_password(user_obj.password), email=user_obj.username)
    from app.services.authenticate import create_access_token
    access_token = create_access_token(
        data={"email": user_obj.nickname, "username": user_obj.username})
    return {"code": 0, "msg": "success", "data": {"Oauth-Token": access_token, "exprie": 60*60*24*7}}


async def get_user_by_username(username: str):
    return await User.objects.filter(username=username).limit(1).all()


async def get_user_by_id(id: int):
    return await User.objects.get(id=id)


async def get_user_info(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception
    user = await get_user_by_username(username=username)
    if not user:
        raise credentials_exception
    return user[0]


def generate_code():
    code = ""
    for i in range(6):
        code += str(random.randint(0, 9))

    return code


async def save_code(user_id: int, code: str):
    user = await get_user_by_id(user_id)
    v_code = await ActivationCode.objects.filter(user_id=user).all()
    if v_code:
        await v_code[0].update(code=code)
    else:
        await ActivationCode.objects.create(user_id=user, code=code)
