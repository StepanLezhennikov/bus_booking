from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Bus
from .schemas import BusCreate


async def create_bus(db: AsyncSession, bus: BusCreate):
    new_bus = Bus(**bus.dict())
    db.add(new_bus)
    await db.commit()
    await db.refresh(new_bus)
    return new_bus


async def get_buses(db: AsyncSession, skip: int = 0, limit: int = 10):
    query = select(Bus).offset(skip).limit(limit)
    result = await db.execute(query)
    buses = result.scalars().all()
    return buses


async def get_bus(bus_id: int, db: AsyncSession):
    query = select(Bus).filter(Bus.id == bus_id)
    bus = await db.execute(query)
    return bus.scalars().first()


async def delete_bus(bus_id: int, db: AsyncSession):
    query = select(Bus).filter(Bus.id == bus_id)
    result = await db.execute(query)
    bus = result.scalar_one_or_none()
    if bus:
        await db.delete(bus)
        await db.commit()
        return bus
    return None
