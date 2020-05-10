from typing import List

from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.response.tags import TagsAllRespose
from app.api.operation.tags import create_tag, get_tags
from app.schemas.tags import Tag, TagCreate

router = APIRouter()


@router.post("/add_tag/", response_model=Tag, tags=['tags'])
async def create_tags(tag: TagCreate):
    return await create_tag(tag.name)


@router.get("/hot", response_model=TagsAllRespose, tags=['tags'])
async def all_tags():
    tags = await get_tags()
    data = [{"id": i.id, "tagName": i.name,"avatar":i.avatar, "createTime": i.created_at.strftime("%Y-%m-%d %H:%M:%S")} for i in tags]
    return {"data": data}
