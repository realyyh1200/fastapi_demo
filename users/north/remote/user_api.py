from fastapi import APIRouter
from ..contract.response import ResponseModel, RegisterUser


user_router = APIRouter()


@user_router.post("/register", response_model=ResponseModel)
async def root(register: RegisterUser):
    pass

