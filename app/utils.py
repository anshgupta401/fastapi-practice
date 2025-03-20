from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
import jwt
from app.config.db import SessionLocal
from passlib.context import CryptContext
from app.config.secrets import settings







pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_session():
    async with SessionLocal() as session:
        yield session
        await session.commit()
        await session.close()




def get_hashed_password(plain_password: str):
    return pwd_context.hash(plain_password)

def verify_password(plain_password: str, password_hashed: str):
    return pwd_context.verify(plain_password,password_hashed)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def decode_jwt(jwt_token: str):
    payload = jwt.decode(jwt_token, settings.SECRET_KEY, settings.ALGORITHM)
    print(payload)
    print(type(payload))
    email = payload.get("email")
    return email




