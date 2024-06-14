from datetime import datetime, timedelta
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import jwt

from fastapi.exceptions import HTTPException

from app.desing_patterns.creational_patterns.singleton.database_singleton import DatabaseSingleton
from app import config


__author__ = "Ricardo Robledo"
__version__ = "1.0"
__all__ = ["create_code", "create_tokens"]


def create_code(id:int, username:str):
    """
    This function creates jwt token being a code for authentication
    
    :param id: the user id
    :param username: the user username
    :return: a jwt token being a code for authentication
    """

    return jwt.encode({'id':id, 'username':username, 'exp':datetime.now()+timedelta(seconds=config.CODE_EXPIRE_SECONDS)}, config.SECRET_KEY, algorithm=config.HASH_ALGORITHM)


def create_tokens(token:str):
    """
    This function creates our access and refresh tokens

    :param token: a jwt token with user information
    :return: a tuple with our access and refresh tokens
    """

    decoded_token = decode_token(token)

    payload = {
        "id": decoded_token['id'],
        "username": decoded_token['username'],
    }

    access_token = jwt.encode({**payload, 'exp':datetime.now()+timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_SECONDS)}, config.SECRET_KEY, algorithm=config.HASH_ALGORITHM)
    refresh_token = jwt.encode({**payload, 'exp':datetime.now()+timedelta(minutes=config.REFRESH_TOKEN_EXPIRE_SECONDS)}, config.SECRET_KEY, algorithm=config.HASH_ALGORITHM)

    return access_token, refresh_token


def decode_token(token:str):
    """
    This function verify that a token is valid

    :param token: a jwt token with user information
    :return: a decoded jwt token
    """

    try:

        return jwt.decode(token, config.SECRET_KEY, algorithms=config.HASH_ALGORITHM)

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')
