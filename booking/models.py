# from sqlalchemy.orm import relationship
#
# from database import Base
# from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
# from sqlalchemy.sql import func
#
#
# class Booking(Base):
#     __tablename__ = "booking"
#
#     id = Column(Integer, primary_key=True, index=True)
#     route_id = Column(Integer, ForeignKey('routes.id'))
#     bus_id = Column(Integer, ForeignKey('buses.id'))
#     user_id = Column(Integer, ForeignKey('users.id'))
#     booking_time = Column(TIMESTAMP, server_default=func.now())
#
#     bus = relationship("Bus", back_populates="booking")
#     route = relationship("Route", back_populates="booking")
#     user = relationship("User", back_populates="bookings")
#
#
#
#
