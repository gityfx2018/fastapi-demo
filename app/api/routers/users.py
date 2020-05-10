from fastapi import Depends, APIRouter, Path, Query, Body
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse

from app.schemas import user, token_sa
from app.response.users import UserCreateResponse, UserCurrentResponse
from app.services.authenticate import authenticate_user, create_access_token
from app.api.operation.users import create_user, get_user_by_username, get_user_info, get_user_by_id
from app.services.jwt import oauth2_scheme
from app.services.smtp import async_send_message

router = APIRouter()


@router.post("/create/", response_model=UserCreateResponse, tags=['users'])
async def create_users(iuser: user.UserCreate):
    ouser = await get_user_by_username(iuser.username)
    if ouser:
        raise HTTPException(
            status_code=400,
            detail="username has been used !!"
        )
    return await create_user(iuser)


@router.post("/login/", response_model=UserCreateResponse, tags=['users'])
# async def user_login(user: OAuth2PasswordRequestForm = Depends()):
async def user_login(*, username: str = Body(...), password: str = Body(...)):
    user = await authenticate_user(username, password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"email": user[0].email, "username": user[0].username})
    # return {"token": 1, "token_type": "bearer"}
    return {"code": 0, "msg": "success", "data": {"Oauth-Token": access_token, "exprie": 86400 * 7}}


@router.get("/current/", response_model=UserCreateResponse, tags=['users'])
async def get_info(user: user.User = Depends(get_user_info)):
    content = {
        "code": 0,
        "msg": "success",
        "data": {
            "id": user.id,
            "avatar": user.avatar,
            "username": user.username,
            "nickname": user.nickname
        }
    }
    return JSONResponse(content=content)


@router.get("/send/", tags=['users'])
async def send_email(user: user.UserActivated = Depends(get_user_info)):
    if user.is_active:
        return JSONResponse(content="账户已激活！")
    async_send_message.delay(id=user.id, email=user.email)
    return JSONResponse(content={"msg": "邮件已发送，请尽快激活您的账户", "code": 0})


@router.get("/activated/{id}", tags=['users'])
async def activate(id: int = Path(..., gt=0, title="账户id"), q: str = Query(..., alias="code", len=6)):
    user = await get_user_by_id(id=id)
    await user.update(is_active=1)
    return JSONResponse(content={"msg": "成功激活", "code": 0})
