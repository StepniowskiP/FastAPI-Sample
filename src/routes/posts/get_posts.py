from json import JSONDecodeError
from typing import List, Dict, Union
from src.app import app
import json
from fastapi import HTTPException

TAGS = ["POSTS"]
ROUTE_PREFIX = "/posts/"


@app.get(path=ROUTE_PREFIX, description="Get all posts", tags=TAGS)
async def get_all_posts() -> List[Union[Dict, None]]:
    with open("./src/mock/posts.json", "r") as json_mock:
        try:
            return json.load(json_mock)
        except JSONDecodeError:
            return []


@app.get(path=ROUTE_PREFIX + "{post_id}", description="Get post by id", tags=TAGS)
async def get_post_by_id(post_id: int) -> Dict:
    json_data = await get_all_posts()
    if 0 <= post_id <= len(json_data):
        return [post for iterator, post in enumerate(json_data) if json_data[iterator]["id"] == post_id][0]

    if post_id < 0:
        raise HTTPException(status_code=404, detail="Provide correct post number (greater or equal to 0)")
    else:
        raise HTTPException(status_code=404, detail="Post with a given id could not be found")
