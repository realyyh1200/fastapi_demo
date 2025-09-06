from fastapi import APIRouter, Form
from ..contract.user_local_cmd import ResponseModel
from ..local.user_local_service import UserLocalService


user_router = APIRouter()


@user_router.post("/register", response_model=ResponseModel)
def root(user_name: str = Form(...), password: str = Form(...)):
    user_local_service = UserLocalService()
    result = user_local_service.register_user(user_name, password)
    if result:
        return ResponseModel(code=200, message="Registered successfully")
    return ResponseModel(code=400, message="bad request")


@user_router.post("/login", response_model=ResponseModel)
def login(user_name: str = Form(...), password: str = Form(...)):
    user_local_service = UserLocalService()
    result = user_local_service.login_user(user_name, password)
    if result is None:
        return ResponseModel(code=400, message="login failed")
    return ResponseModel(code=200, message=result)

