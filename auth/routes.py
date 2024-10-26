from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from .models import User
from .schemas import Token, TokenData
from .auth import create_access_token, authenticate_user, get_current_user, oauth2_scheme
from fastapi.security import OAuth2PasswordRequestForm
from .user_crud import create_user
from .user_schemas import UserCreate, UserBase

router = APIRouter()


@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Неверный логин или пароль")
    access_token = create_access_token(data={"sub": user.username, "role": user.role.value})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", response_model=UserBase)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await db.execute(select(User).filter(User.username == user.username))
    if existing_user.scalar():
        raise HTTPException(status_code=400, detail="Пользователь с таким именем уже существует")

    return await create_user(user, db)


# @router.get('/current_user', response_model=UserBase)
# async def get_user(token: str = Depends(oauth2_scheme)):
#     return get_current_user(token)
