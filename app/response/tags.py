from typing import List

from .baseresponse import BaseModelResponse


class TagsAllRespose(BaseModelResponse):
    data: List[dict] = []
