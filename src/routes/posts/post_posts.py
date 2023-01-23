import json

from src.app import app
from .get_posts import get_all_posts
from src.models.post_schema import (
    KeywordPostSchema,
    PostSchema
)
from fastapi import HTTPException

TAGS = ["POSTS"]
ROUTE_PREFIX = "/posts/"


@app.post(ROUTE_PREFIX + "{keyword}", description="Get post by content keywords", tags=TAGS)
async def get_post_by_keywords(keywords: KeywordPostSchema):
    json_data = await get_all_posts()
    posts = []
    for iterator, post in enumerate(json_data):
        for keyword in keywords.keywords:
            if post["content"].find(keyword) != -1 and post not in posts:
                posts.append(post)

    if not posts:
        raise HTTPException(status_code=404, detail="No posts can be found with given keywords")

    return posts


@app.post(ROUTE_PREFIX, description="Post a new post", tags=TAGS)
async def create_new_post(post: PostSchema):
    pass
    json_data = await get_all_posts()

    post.id = len(json_data) + 1
    json_data.append(PostSchema.serialize(post))
    print(json_data)
    with open("./src/mock/posts.json", "w") as file:
        try:
            file.write(json.dumps(json_data, indent=4))
        except IOError:
            raise HTTPException(status_code=500, detail="Sth went wrong during adding post")
        else:
            return {"status": 200,
                    "message": "Post added"}



