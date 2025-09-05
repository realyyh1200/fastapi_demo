from pydantic import BaseModel

class RegisterUserCmd(BaseModel):
    user_name: str
    password: str

class ResponseModel(BaseModel):
    code: int
    message: str