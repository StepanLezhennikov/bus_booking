from sqlalchemy import Column, Integer, String, event
from sqlalchemy.orm import relationship

from database import Base


class Bus(Base):
    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    seats = Column(Integer)
    free_seats = Column(Integer)

    routes = relationship("Route", back_populates="bus")
    # booking = relationship("Booking", back_populates="bus")


@event.listens_for(Bus, 'before_insert')
def set_free_seats(mapper, connect, target):
    target.free_seats = target.seats
