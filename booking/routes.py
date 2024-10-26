from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.auth import get_current_user
from auth.models import User
from auth.user_schemas import UserBase
from booking.schemas import BookingCreate, Booking as SBooking
from database import get_db
from .crud import add_booking as create_booking

router = APIRouter(prefix='/booking', tags=["Работа с бронированием"])


@router.post('/', response_model=SBooking)
async def add_booking(booking: BookingCreate, user: UserBase = Depends(get_current_user),
                      db: AsyncSession = Depends(get_db)):
    query = select(User.id).filter(User.username == user['username'])
    res = await db.execute(query)
    user_id = res.scalar_one_or_none()
    if not user_id:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    booking_data = booking.copy(update={"user_id": user_id})
    return await create_booking(booking_data, db)
