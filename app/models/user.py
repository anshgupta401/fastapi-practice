








from datetime import datetime
from sqlalchemy import DateTime, Enum, Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from enum import Enum as pyEnum
from app.config.db import Base




class User(Base):
    __tablename__ = "users"
    

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String[100])
    email: Mapped[str] = mapped_column(String[100],unique=True)
    city: Mapped[str] = mapped_column(String[100], nullable= True,)
    address: Mapped[str] = mapped_column(String, nullable= True)
    zip_code: Mapped[int] = mapped_column(Integer, nullable= True)
    password_hashed: Mapped[str] = mapped_column(String)