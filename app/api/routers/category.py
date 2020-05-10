from fastapi import APIRouter

from app.schemas.category import CateGoryCreate
from app.api.operation.category import create_category, all_categorys
from app.response.category import CategoryAllResponse

router = APIRouter()


@router.post("/create/", tags=['category'])
async def createCategory(cate: CateGoryCreate):
    return await create_category(cate)


@router.get("/detail/", response_model=CategoryAllResponse, tags=['category'])
async def allCategorys():
    data = await all_categorys()
    data = [{"id": i.id, "categoryName": i.category_name, "avatar": i.avatar, "description": i.description}
            for i in data]
    return {"data": data}
