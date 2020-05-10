from typing import List

from .baseresponse import BaseModelResponse


class CategoryAllResponse(BaseModelResponse):
    data: List[dict] = []
