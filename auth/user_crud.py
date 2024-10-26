from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .auth import get_password_hash
from auth.user_schemas import UserCreate
from .models import User


async def create_user(user: UserCreate, db: AsyncSession):
    hashed_pass = get_password_hash(user.password)
    new_user = User(username=user.username, email=user.email, password_hash=hashed_pass)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
