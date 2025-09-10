from fastapi import APIRouter
from users.north.remote.user_api import user_router
from ai_coding.north.remote.ai_coding_api import ai_coding_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(ai_coding_router, prefix="/aicoding", tags=["aicoding"])
