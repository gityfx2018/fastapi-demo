import jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

SECRET_KEY = "hsdkfjsgIHJJKSDFHG4385eutioudhgj1sdfjGszd>'>qz56.,/hds?k"
ALGORITHM = "HS256"


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")  # 加密 解密


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password):
    return pwd_context.hash(password)
