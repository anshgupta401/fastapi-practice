


from fastapi import APIRouter
from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.user import router as user_router

api_router = APIRouter()
api_router.include_router(auth_router,prefix="/auth",tags=["Auth"])
api_router.include_router(user_router,prefix="/users",tags=["Users"])