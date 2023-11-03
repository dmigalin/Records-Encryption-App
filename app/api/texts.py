from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.texts import TextSchemaCreate
from api.dependencies import text_service
from services.texts import TextService
from db.pgs import get_async_session

router = APIRouter(
    tags=["Records"],
)

@router.post("/create_record/")
async def create_record(
    data: TextSchemaCreate,
    text_service: Annotated[TextService, Depends(text_service)],
    session: Annotated[AsyncSession, Depends(get_async_session)]):
    res = await text_service.create_record(session, data)
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
    text_service: Annotated[TextService, Depends(text_service)],
    session: Annotated[AsyncSession, Depends(get_async_session)]):
    res = await text_service.update_records(session)
    print('[+] ' + res)
    return res