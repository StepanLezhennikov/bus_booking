from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

from database import Base


class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    from_city = Column(String)
    to_city = Column(String)
    departure_time = Column(TIMESTAMP)
    arrival_time = Column(TIMESTAMP)

    bus_id = Column(Integer, ForeignKey("buses.id"))

    bus = relationship("Bus", back_populates='routes')
