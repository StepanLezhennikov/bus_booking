from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from auth.auth import role_required
from database import get_db
from .schemas import Bus, BusCreate
from .crud import create_bus as create_new_bus, get_buses as get_all_buses, get_bus as get_one_bus, delete_bus as delete_one_bus

router = APIRouter(prefix="/buses", tags=["Работа с автобусами"])


@router.post('/', dependencies=[Depends(role_required('admin'))], description='Создание автобуса')
async def create_bus(bus: BusCreate, db: AsyncSession = Depends(get_db)) -> Bus:
    new_bus = await create_new_bus(db, bus)
    return Bus.from_orm(new_bus)


@router.get('/', description='Получение всех автобусов')
async def get_buses(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)) -> List[Bus]:
    return await get_all_buses(db, skip=skip, limit=limit)


@router.get('/{bus_id}', description='Получение одного автобуса')
async def get_bus(bus_id: int, db: AsyncSession = Depends(get_db)) -> Bus:
    bus = await get_one_bus(bus_id, db)
    if not bus:
        raise HTTPException(status_code=404, detail="Автобус не найден")
    return bus


@router.delete('/{bus_id}', dependencies=[Depends(role_required('admin'))], description="Удаление автобуса")
async def delete_bus(bus_id: int, db: AsyncSession = Depends(get_db)) -> Bus:
    bus = await  delete_one_bus(bus_id, db)
    if not bus:
        raise HTTPException(status_code=404, detail="Автобус не найден")
    return bus
