from src.app import app

TAGS = ["HOMEPAGE"]
ROUTE_PREFIX = "/"


@app.get(path=ROUTE_PREFIX, description="Just a simple homepage that returns message.", tags=TAGS)
def homepage() -> str:
    return "Great, Homepage works!"
