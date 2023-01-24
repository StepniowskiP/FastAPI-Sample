from fastapi import FastAPI
from src.models.config_schema import ConfigModel
from decouple import config

# fetch config
config = ConfigModel(
    secret=config("SECRET"),
    algorithm=config("ALGORITHM"),
    expiration_time=config("EXPIRATION_TIME")
)

# instantiate app
app = FastAPI(
    title="FastAPI sample",
    description="FastAPI sample with JWT authentication",
    docs_url="/api/v1/",
    version="0.0.1",
)
