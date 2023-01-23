from src.app import app

TAGS = ["HOMEPAGE"]
ROUTE_PREFIX = "/"


@app.get(ROUTE_PREFIX, description="Just a simple homepage that returns message.", tags=TAGS)
def homepage():
    return "Great, Homepage works!"
