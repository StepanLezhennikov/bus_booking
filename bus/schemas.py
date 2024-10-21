from pydantic import BaseModel


class BusBase(BaseModel):
    name: str
    seats: int


class BusCreate(BusBase):
    pass


class Bus(BusBase):
    id: int

    class Config:
        from_attributes = True
