


from fastapi import APIRouter, Depends, HTTPException

from app.crud.user import delete_user, get_all_users, get_user_by_id
from app.deps import get_current_user
from app.models.user import User
from app.schemas.user import UserOut
from app.utils import get_session
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


@router.get("/", response_model= list[UserOut])
async def get_users(db: AsyncSession = Depends(get_session)):
    all_users = await get_all_users(db)
    if not all_users:
        return []
    return all_users



@router.get("/{user_id}", response_model=UserOut)
async def get_user_profile(user_id: int, db: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    if user.id != user_id:
        raise HTTPException(status_code=401,detail="Permission Denied")
    user_exists = await get_user_by_id(user_id,db)
    if not user_exists:
        raise HTTPException(status_code=404, detail="User not Found")
    return user_exists

@router.delete("/{user_id}")
async def delete_user_profile(user_id: int, db: AsyncSession = Depends(get_session)):
    user_exists = await get_user_by_id(user_id,db)
    if not user_exists:
        raise HTTPException(status_code=404, detail="User not Found")
    await delete_user(user_exists,db)
    return "User has been deleted Successfully"