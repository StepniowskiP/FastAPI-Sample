from pydantic import BaseModel, Field, validator
from re import match
from typing import Union, Dict


class UserSchema(BaseModel):
    full_name: str = Field(default=None)
    email: Union[str, Dict[str, str]] = Field(default=None)
    password: Union[str, Dict[str, str]] = Field(default=None)
    token: str = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "full_name": "Example",
                "email": "example@example.com",
                "password": "Password123@"
            }
        }

    @validator("email")
    @classmethod
    def email_validator(cls, value):
        email_regex = "[\w\.-]+@[\w\.-]+\.[A-Za-z]{2,3}$"
        errors = []
        if not match(email_regex, value):
            return {"ValidationError": f"Wrong email structure: {value}"}
        return value if not errors else errors

    @validator("password")
    @classmethod
    def password_validator(cls, value):
        password_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if not match(password_regex, value):
            return {"ValidationError": "Password must contain minimum eight characters, at least one uppercase letter, "
                                       "one lowercase letter, one number and one special character"}
        return value

    def serialize(self):
        return {
            "full_name": self.full_name,
            "email": self.email,
            "password": self.password,
            "token": self.token
        }


class UserLoginSchema(BaseModel):
    email: str = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "email": "john@example.com",
                "password": "password123"
            }
        }
