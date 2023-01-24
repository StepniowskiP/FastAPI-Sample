from json import JSONDecodeError

from src.app import app
import json

TAGS = ["USER"]
ROUTE_PREFIX = "/user/"


@app.get(path=ROUTE_PREFIX, description="Get all users", tags=TAGS)
async def get_all_users():
    with open("./src/mock/users.json", "r") as json_mock:
        try:
            return json.load(json_mock)
        except JSONDecodeError:
            return []