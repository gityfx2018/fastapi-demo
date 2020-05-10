from app.models.article import Tags


async def create_tag(name: str):
    return await Tags.objects.create(name=name)


async def get_tags():
    return await Tags.objects.all()
