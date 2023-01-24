from typing import List, Callable
from .post_user import sign_up_user
from .get_user import  get_all_users

user_routes: List[Callable] = [
    get_all_users,
    sign_up_user
]
