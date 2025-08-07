from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class CreatePost(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    created_at: datetime