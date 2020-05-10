from typing import List

from app.models.article import Articles
from app.schemas.articles import ArticlesCreate


async def create_article(*, title: str, views: int = 0, is_hot: bool = False, content: str,
                         tag_id: int, key_words: List[str] = [], user_id: int):
    await Articles.objects.create(
        title=title, views=views, is_hot=is_hot, content=content, tag_id=tag_id, key_words=key_words, user_id=user_id
    )
