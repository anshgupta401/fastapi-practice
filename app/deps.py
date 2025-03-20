
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.user import get_user_by_email
from app.utils import decode_jwt, get_session





oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(token:str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_session)):
    try: 
        email = decode_jwt(token)
        user = await get_user_by_email(email,db)
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        return user
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="could not validate credentials")