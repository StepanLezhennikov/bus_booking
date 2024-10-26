from fastapi import HTTPException
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from booking.models import Booking
from booking.schemas import BookingCreate
from bus.models import Bus


async def add_booking(booking: BookingCreate, db: AsyncSession):
    query = select(Bus).filter(Bus.id == booking.bus_id, Bus.free_seats > 0)
    res = await db.execute(query)
    bus = res.scalar_one_or_none()
    if not bus:
        raise HTTPException(status_code=404, detail="В этом автобусе нет мест, либо такого автобуса нет")

    new_booking = Booking(**booking.dict())
    db.add(new_booking)
    await db.commit()
    await db.refresh(new_booking)
    await reduce_free_seats_by_one(new_booking.bus_id, db)
    return new_booking


async def reduce_free_seats_by_one(bus_id: int, db: AsyncSession):
    stmt = (
        update(Bus)
        .where(Bus.id == bus_id)
        .values(free_seats=Bus.free_seats - 1)
        .execution_options(synchronize_session="fetch")
    )
    await db.execute(stmt)
    await db.commit()

