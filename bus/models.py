from sqlalchemy import Column, Integer, String
from database import Base


class Bus(Base):
    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    seats = Column(Integer)
