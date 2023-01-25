from pydantic import BaseModel, Field, validator
from src.exceptions.custom_exceptions import ValidationError
from typing import Union


class ConfigModel(BaseModel):
    secret: str = Field(default=None)
    algorithm: str = Field(default=None)
    expiration_time: Union[int, str]

    @validator("secret")
    @classmethod
    def secret_validator(cls, value) -> str:
        if len(value) < 10:
            raise ValidationError(message="Secret must be minimum 10 characters")
        return value

    @validator("algorithm", "secret")
    @classmethod
    def algorithm_validator(cls, value) -> str:
        if value == '':
            raise ValidationError(message=f"Values (algorithm, secret) must not be empty")
        return value

    @validator("expiration_time")
    @classmethod
    def expiration_validator(cls, value) -> int:
        return 1_000_000 if not value else value
