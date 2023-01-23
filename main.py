# noinspection PyUnresolvedReferences
from src.app import app
# noinspection PyUnresolvedReferences
from src.routes.homepage.router import homepage_routes
# noinspection PyUnresolvedReferences
from src.routes.posts.router import posts_routes


if __name__ == "__main__":
    print("App is starting")