


from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    city: str | None = None
    address: str | None = None
    zip_code: int | None = None
    



class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    city: str | None = None
    address: str | None = None
    zip_code: int | None = None