from fastapi import Depends
from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bus.models import Bus
from database import get_db


class RouteBase(BaseModel):
    from_city: str = Field(..., min_length=3, max_length=100)
    to_city: str = Field(..., min_length=3, max_length=100)
    departure_time: datetime = Field(...)
    arrival_time: datetime = Field(...)

    bus_id: int = Field(..., description="ID автобуса, к которому привязан маршрут")

    @field_validator('to_city', 'from_city', mode='after')
    def validate_city(cls, city: str):
        if not city[0].isupper():
            raise ValueError('Название города должно начинаться с большой буквы')
        return city

    class Config:
        from_attributes = True


class RouteCreate(RouteBase):
    @model_validator(mode='before')
    def validate_times(cls, values):
        departure_time = values.get('departure_time')
        arrival_time = values.get('arrival_time')
        if departure_time and arrival_time and departure_time >= arrival_time:
            raise ValueError('Время прибытия должно быть позже времени отправления')
        reformat_time(values)
        return values


class Route(RouteBase):
    id: int


def reformat_time(values):
    if isinstance(values['departure_time'], str):
        departure_time = datetime.fromisoformat(values['departure_time'])
    if isinstance(values['arrival_time'], str):
        arrival_time = datetime.fromisoformat(values['arrival_time'])
    if departure_time:
        values['departure_time'] = departure_time.replace(tzinfo=None)
    if arrival_time:
        values['arrival_time'] = arrival_time.replace(tzinfo=None)
