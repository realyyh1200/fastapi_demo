from fastapi import APIRouter
from ..contract.response import ResponseModel


user_router = APIRouter()


@user_router.get("/")
async def root():
    return ResponseModel(message="Hello World")