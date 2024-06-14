from urllib.parse import urlencode

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app import config


__author__ = "Ricardo Robledo"
__version__ = "1.0"


router = APIRouter(prefix='/frontend')

templates = Jinja2Templates(directory='app/frontend/frontend_templates/templates')


@router.get('/control-panel')
async def get_control_panel_page(request:Request):
    return templates.TemplateResponse('control-panel-login.html', {'request': request})

@router.get('/user-login', status_code=200)
async def get_login_page(request:Request):
    return templates.TemplateResponse('user-login.html', {'request':request, 'callback_url':config.CALLBACK_URL})
