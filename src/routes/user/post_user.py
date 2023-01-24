from src.app import app
from src.models.user_schema import UserSchema, UserLoginSchema
from fastapi import HTTPException, Body
import json
from src.auth.jwt_handler import encode_jwt
from .get_user import get_all_users
from src.app import config

TAGS = ["USER"]
ROUTE_PREFIX = "/user/"


@app.post(path=ROUTE_PREFIX + "signup", description="Sing up endpoint for new user", tags=TAGS)
async def sign_up_user(user: UserSchema = Body(default=None)):
    if "ValidationError" in user.email:
        raise HTTPException(status_code=500, detail=f"Errors occurred during email validation: {user.email}")
    if "ValidationError" in user.password:
        raise HTTPException(status_code=500, detail=f"Errors occurred during password validation: {user.password}")
    json_data = await get_all_users()
    for iterator, user in enumerate(json_data):
        if user["email"] == user.email:
            raise HTTPException(status_code=500, detail="User with given credentials already exists")
    user.token = encode_jwt(user.email, config.expiration_time)
    json_data.append(user.serialize())
    with open("./src/mock/users.json", "w") as file:
        try:
            file.write(json.dumps(json_data, indent=4))
        except IOError:
            raise HTTPException(status_code=500, detail="Sth went wrong during adding user")
        else:
            return {"status": 200,
                    "message": "User added",
                    "token": user.token["token"]}


@app.post(path=ROUTE_PREFIX + "login", description="Login endpoint", tags=TAGS)
async def sign_up_user(user_login: UserLoginSchema = Body(default=None)):
    json_data = await get_all_users()
    for iterator, user in enumerate(json_data):
        print(user)
        if user_login.email == user["email"] and user_login.password == user["password"]:
            return {"status": 200,
                    "message": "User logged in",
                    "token": user["token"]["token"]}

    raise HTTPException(status_code=500, detail="User with given credentials does not exist")
