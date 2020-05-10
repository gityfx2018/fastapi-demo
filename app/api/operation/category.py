from app.models.article import CateGory
from app.schemas.category import CateGoryCreate


async def create_category(category: CateGoryCreate):
    await CateGory.objects.create(
        category_name=category.category_name,
        avatar=category.avatar,
        description=category.description
    )


async def all_categorys():
    return await CateGory.objects.all()
