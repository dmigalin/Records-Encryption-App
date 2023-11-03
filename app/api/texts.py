from typing import Annotated
from fastapi import APIRouter, Depends

from schemas.texts import TextSchemaCreate
from api.dependencies import text_service
from services.texts import TextService

router = APIRouter(
    tags=["Records"],
)

@router.post("/create_record/")
async def create_record(
    data:TextSchemaCreate,
    text_service: Annotated[TextService, Depends(text_service)]): 
    res = await text_service.create_record(data)
    return res

@router.get("/get_record/")
async def get_record(
    object_id:str,
    password: str,
    text_service: Annotated[TextService, Depends(text_service)]):
    res = await text_service.get_record(object_id,password)
    return res

@router.get("/update_records/")
async def update_records(
    text_service: Annotated[TextService, Depends(text_service)]):
    res = await text_service.update_records()
    print('[+] ' + res)
    return res

