from fastapi import APIRouter
from ..contract.user_local_cmd import ResponseModel, RegisterUserCmd, LoginUserCmd
from ..local.user_local_service import UserLocalService


user_router = APIRouter()


@user_router.post("/register", response_model=ResponseModel)
def root(register: RegisterUserCmd):
    user_local_service = UserLocalService()
    result = user_local_service.register_user(register)
    if result:
        return ResponseModel(code=200, message="Registered successfully")
    return ResponseModel(code=400, message="bad request")


@user_router.post("/login", response_model=ResponseModel)
def login(login_cmd: LoginUserCmd):
    user_local_service = UserLocalService()
    result = user_local_service.login_user(login_cmd)
    if result is None:
        return ResponseModel(code=400, message="login failed")
    return ResponseModel(code=200, message=result)
