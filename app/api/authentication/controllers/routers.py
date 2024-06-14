from typing import Annotated, Union

from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import JSONResponse

from ..utils import token_handlers
from app.desing_patterns.creational_patterns.singleton.database_singleton import DatabaseSingleton
from app.api.authentication.utils import password_handlers
from app import config
from ..schemas.schema import UserRequestModel


__author__ = 'Ricardo Robledo'
__version__ = '1.0'


router = APIRouter(prefix='/authentication', tags=['OAuth2'])


@router.post('/oauth/authorize', status_code=200)
async def get_code(user:UserRequestModel):

    user_exists = await DatabaseSingleton.is_existing_user(user.username)

    if not user_exists:
        raise HTTPException(status_code=404, detail='credentials not found')

    user_found = await DatabaseSingleton.get_active_user(user.username)
    password_matched = password_handlers.verify_password(user.password, user_found.password)

    if not password_matched:
        raise HTTPException(status_code=404, detail='credentials not found')

    return {'code':token_handlers.create_code(user_found.id, user_found.username)}


@router.post('/oauth/token', status_code=200)
async def get_tokens(request:Request):

    form = await request.form()

    if not 'grant_type' in form:
        raise HTTPException(status_code=404, detail='grant_type not found')
    
    tokens = None

    if form['grant_type']=='authorization_code':
        tokens = token_handlers.create_tokens(form['code'])
    elif form['grant_type']=='resfresh_token':
        tokens = token_handlers.create_tokens(form['refresh_token'])

    return JSONResponse(content={'token_type':'bearer', 'access_token':tokens[0], 'refresh_token':tokens[1], 'expires_in':config.ACCESS_TOKEN_EXPIRE_SECONDS})
