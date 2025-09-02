from fastapi import APIRouter, Depends, HTTPException
from users.north.remote.user_api import user_router

router = APIRouter()


router.include_router(user_router)
