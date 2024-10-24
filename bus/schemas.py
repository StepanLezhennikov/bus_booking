from pydantic import BaseModel, Field, validator, field_validator


class BusBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    seats: int = Field(..., gt=0, lt=100)

    @field_validator('name')
    def validate_name(cls, name: str):
        if not name[0].isupper():
            raise ValueError('Первый символ должен быть заглавным')
        return name

    class Config:
        from_attributes = True


class BusCreate(BusBase):
    pass


class Bus(BusBase):
    id: int

    class Config:
        from_attributes = True
