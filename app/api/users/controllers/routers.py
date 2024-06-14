from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, Response, RedirectResponse, JSONResponse

from ..services import user_action_service


router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/user-action', status_code=200)
async def post_register_action(request:Request):

    await user_action_service.post_register_action(1, str(request.method), str(request.url.path), 200)

    return {}
