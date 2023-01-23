from typing import List, Callable
from .get_posts import (
    get_all_posts,
    get_post_by_id
)

from .post_posts import (
    get_post_by_keywords,
    create_new_post
)

posts_routes: List[Callable] = [
    get_all_posts,
    get_post_by_id,
    get_post_by_keywords,
    create_new_post
]
