import jwt

from fastapi import APIRouter, Request, Query, Depends
from fastapi.exceptions import HTTPException

from ..services import training_service
from app.api.base.controllers.general_middlewares import get_authorization_token


router = APIRouter(prefix='/training', tags=['Training'])


@router.get('/document', status_code=200)
async def get_training_document(
    token:str=Depends(get_authorization_token),
    topic_name:str=Query(..., title='Tema del documento', description='Tema del documento a buscar'),
    document_name:str=Query(..., title='Nombre del documento', description='Nombre del documento a buscar')):

    training_document = await training_service.get_training_document(topic_name, document_name)

    if training_document is None:
        raise HTTPException(status_code=404, detail='Documento no encontrado')

    return {'documento': training_document}


@router.get('/workshop', status_code=200)
async def get_course():

    course = await training_service.get_workshop()

    return {'workshop': course}
