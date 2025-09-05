from fastapi import APIRouter
from ..contract.user_local_cmd import ResponseModel, RegisterUserCmd
from ..local.user_local_service import UserLocalService


user_router = APIRouter()


@user_router.post("/register", response_model=ResponseModel)
def root(register: RegisterUserCmd):
    user_local_service = UserLocalService()
    result = user_local_service.register_user(register)
    if result:
        return ResponseModel(code=200, message="Registered successfully")
    return ResponseModel(code=400, message="bad request")
