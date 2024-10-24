from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from bus.models import Bus


async def validate_bus_id(bus_id: int, db: AsyncSession):
    if bus_id < 0:
        raise HTTPException(status_code=400, detail="Bus_id не должен быть отрицательным")

    query = select(Bus).filter(Bus.id == bus_id)
    result = await db.execute(query)
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Автобуса с таким id нет")
