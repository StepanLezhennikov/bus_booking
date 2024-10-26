# from typing import Optional
#
# from pydantic import BaseModel, Field
# from datetime import datetime
#
#
# class BookingBase(BaseModel):
#     route_id: int = Field(...)
#     bus_id: int = Field(...)
#     user_id: int = Field(...)
#     booking_time: Optional[datetime] = None
#
#
# class BookingCreate(BookingBase):
#     pass
#
#
# class Booking(BookingBase):
#     id: int
