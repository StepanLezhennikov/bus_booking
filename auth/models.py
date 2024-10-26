from enum import Enum as EnumPy

from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Column, Integer, String, Enum, Boolean


class UserRole(EnumPy):
    admin = "admin"
    client = "client"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(Enum(UserRole), default=UserRole.admin)  # Потом исправить на client
    is_active = Column(Boolean, default=True)

    bookings = relationship("Booking", back_populates="user")
