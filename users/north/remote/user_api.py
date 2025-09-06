from typing import Annotated

from fastapi import APIRouter, Form, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from ..contract.user_local_cmd import ResponseModel, Token
from ..local.user_local_service import UserLocalService, get_current_user


user_router = APIRouter()


@user_router.post("/register", response_model=ResponseModel)
def root(username: str = Form(...), password: str = Form(...)):
    user_local_service = UserLocalService()
    result = user_local_service.register_user(username, password)
    if result:
        return ResponseModel(code=200, message="Registered successfully")
    return ResponseModel(code=400, message="bad request")


@user_router.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user_local_service = UserLocalService()
    access_token = user_local_service.login_user(form_data.username, form_data.password)
    if access_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return Token(access_token=access_token, token_type="bearer")


@user_router.post("/hello", response_model=ResponseModel)
def hello(username: str = Depends(get_current_user)):
    return ResponseModel(code=200, message=f"Hello {username}")
