from fastapi import FastAPI


app = FastAPI(
    title="FastAPI sample",
    description="FastAPI sample with JWT authentication",
    docs_url="/api/v1/",
    version="0.0.1",
)
