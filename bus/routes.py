from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from .schemas import Bus, BusCreate
from .crud import create_bus as create_new_bus

router = APIRouter(tags=["Работа с автобусами"])


@router.post('/buses/')
async def create_bus(bus: BusCreate, db: AsyncSession = Depends(get_db)) -> Bus:
    new_bus = await create_new_bus(db, bus)
    return Bus.from_orm(new_bus)


