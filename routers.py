from fastapi import APIRouter
from users.north.remote.user_api import user_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["users"])
