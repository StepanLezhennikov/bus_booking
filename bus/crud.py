from sqlalchemy.ext.asyncio import AsyncSession
from .models import Bus
from .schemas import BusCreate


async def create_bus(db: AsyncSession, bus: BusCreate):
    new_bus = Bus(**bus.dict())
    db.add(new_bus)
    await db.commit()
    await db.refresh(new_bus)
    return new_bus
