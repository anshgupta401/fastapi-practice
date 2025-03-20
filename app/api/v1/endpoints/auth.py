from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.crud.user import create_user, get_user_by_email
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils import create_access_token, get_session, verify_password
from app.config.secrets import settings

router = APIRouter()



@router.post("/")
async def create_user_endpoint(user_create: UserCreate, db: AsyncSession = Depends(get_session)):
    user_exists = await get_user_by_email(user_create.email,db)
    if user_exists:
        raise HTTPException(status_code=403, detail="Email Already Exists")
    create_user(user_create,db)
    return "User has Been created successfully"

@router.post("/login")
async def login(user_login: UserLogin, db: AsyncSession = Depends(get_session)):
    user_exists = await get_user_by_email(user_login.email,db)
    if not user_exists:
        raise HTTPException(status_code=403, detail="Email/Password Not Valid")
    password_exists = verify_password(user_login.password, user_exists.password_hashed)
    if not password_exists:
        raise HTTPException(status_code=403, detail="Email/Password Not Valid")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"email": user_exists.email}, expires_delta=access_token_expires)
    
    return {"access_token":access_token, "token_type":"Bearer"}
