from fastapi import HTTPException, Header


__author__ = 'Ricardo Robledo'
__version__ = '1.0'


def get_authorization_token(authorization: str = Header(None)):

    if authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header is missing")
    
    scheme, _, token = authorization.partition(' ')

    if not scheme or scheme.lower() != 'bearer':
        raise HTTPException(status_code=401, detail="Unauthorized or malformed Authorization header")

    return token
