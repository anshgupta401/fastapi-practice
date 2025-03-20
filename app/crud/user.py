

from fastapi import Depends
from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils import get_hashed_password, get_session


def create_user(user_create: UserCreate, db: AsyncSession = Depends(get_session)):
    passwordhash = get_hashed_password(user_create.password)
    new_user = User(name = user_create.name, email = user_create.email,city = user_create.city, address = user_create.address, zip_code = user_create.zip_code, password_hashed = passwordhash)
    db.add(new_user)
    db.commit()

async def get_all_users(db: AsyncSession = Depends(get_session)):
    query = select(User)
    users = await db.execute(query)
    return users.scalars().all()

async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_session)):
    query = select(User).where(User.id == user_id)
    user = await db.execute(query)
    return user.scalars().first()

async def get_user_by_email(email: EmailStr, db: AsyncSession = Depends(get_session)):
    query = select(User).where(User.email == email)
    user = await db.execute(query)
    return user.scalars().first()

async def delete_user(user: User, db: AsyncSession = Depends(get_session)):
    await db.delete(user)
    return None

