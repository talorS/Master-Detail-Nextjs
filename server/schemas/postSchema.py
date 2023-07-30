from typing import Optional
from pydantic import BaseModel


class NewPost(BaseModel):
    title: str
    content: str


class UpdatePost(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
