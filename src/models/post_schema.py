from pydantic import BaseModel, Field, validator
from typing import List, Union, Dict


class PostSchema(BaseModel):
    id: int = Field(default=None, gt=0)
    title: Union[str, Dict[str, str]] = Field(default=None)
    content: str = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "title": "Some title",
                "content": "some content about sth"
            }
        }

    @validator('title')
    @classmethod
    def title_validator(cls, value):
        if not value[0].isupper():
            return {"ValidationError": "Title must start with a capital letter"}
        return value

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content
        }


class KeywordPostSchema(BaseModel):
    keywords: List[str] = Field(default_factory=list)

    class Config:
        schema_extra = {
            "example": {
                "keywords": ['some', 'keyword']
            }
        }
