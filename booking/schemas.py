from typing import Optional

from pydantic import BaseModel, Field, model_validator
from datetime import datetime


class BookingBase(BaseModel):
    route_id: int = Field(...)
    bus_id: int = Field(...)
    booking_time: Optional[datetime] = None


class BookingCreate(BookingBase):
    @model_validator(mode='before')
    def validate_times(cls, values):
        if 'booking_time' in values and isinstance(values['booking_time'], str):
            try:
                booking_time = datetime.fromisoformat(values['booking_time'])
                values['booking_time'] = booking_time.replace(tzinfo=None)
            except ValueError:
                raise ValueError("Некорректный формат времени")
        return values


class Booking(BookingBase):
    id: int
