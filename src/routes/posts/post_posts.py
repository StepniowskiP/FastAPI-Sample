import json

from src.app import app
from .get_posts import get_all_posts
from src.models.post_schema import (
    KeywordPostSchema,
    PostSchema
)
from fastapi import HTTPException, Body, Depends
from typing import Dict
from src.auth.jwt_bearer import JwtBearer

TAGS = ["POSTS"]
ROUTE_PREFIX = "/posts/"


@app.post(path=ROUTE_PREFIX + "{keyword}", description="Get post by content keywords", tags=TAGS)
async def get_post_by_keywords(keywords: KeywordPostSchema = Body(default=None)):
    json_data = await get_all_posts()
    posts = []
    for iterator, post in enumerate(json_data):
        for keyword in keywords.keywords:
            if post["content"].find(keyword) != -1 and post not in posts:
                posts.append(post)

    if not posts:
        raise HTTPException(status_code=404, detail="No posts can be found with given keywords")

    return posts


@app.post(path=ROUTE_PREFIX, description="Post a new post", tags=TAGS, dependencies=[Depends(JwtBearer())])
async def create_new_post(post: PostSchema = Body(default=None)) -> Dict:
    pass
    json_data = await get_all_posts()

    if "ValidationError" in post.title:
        raise HTTPException(status_code=500, detail=post.title)

    post.id = len(json_data) + 1
    json_data.append(PostSchema.serialize(post))
    with open("./src/mock/posts.json", "w") as file:
        try:
            file.write(json.dumps(json_data, indent=4))
        except IOError:
            raise HTTPException(status_code=500, detail="Sth went wrong during adding post")
        else:
            return {"status": 200,
                    "message": "Post added"}



