import aiofiles
from fastapi import APIRouter, Depends, UploadFile, File
from starlette.responses import JSONResponse

from app.api.operation.articles import create_article
from app.api.operation.users import get_user_info
from app.schemas.articles import Articles, ArticlesCreate
from app.schemas.user import User

router = APIRouter()


@router.post("/create_articles/", response_model=Articles, tags=['articles'])
async def articles(article: ArticlesCreate, user: User = Depends(get_user_info)):
    return await create_article(title=article.title, content=article.content, tag_id=article.tag_id, key_words=article.key_words, user_id=article.user_id)


@router.post("/upload/", tags=['articles'])
async def upload_file(file: UploadFile=File(...), user: User=Depends(get_user_info)):
    content = await file.read()
    async with aiofiles.open(f'app/files/{file.filename}', 'w+', encoding="utf-8") as f:
        await f.write(content.decode())
    return JSONResponse(content={"msg": file.filename, "code": 0})
