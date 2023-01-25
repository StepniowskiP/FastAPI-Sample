# Responsible for encoding, decoding, signing and returning JWT

import time
import jwt
from src.app import config
from typing import Dict


def __token_response(token: str) -> Dict[str, str]:
    """
    Returns token
    """
    return {
        "token": token
    }


def encode_jwt(user_id: str, expiration: int) -> Dict[str, str]:
    """
    Encodes Json Web Token
    """

    payload = {
        "userID": user_id,
        "expiration_date": time.time() + expiration
    }
    token = jwt.encode(
        payload=payload,
        key=config.secret,
        algorithm=config.algorithm
    )
    return __token_response(token)


def decode_jwt(token: str) -> str:
    decoded_token = jwt.decode(token, config.secret, config.algorithm)
    return decoded_token if decoded_token["expiration_date"] >= time.time() else None


def is_jwt_valid(token: str) -> bool:
    payload = decode_jwt(token)
    return True if payload else False
