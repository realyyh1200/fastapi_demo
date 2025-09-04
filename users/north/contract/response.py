from pydantic import BaseModel

class RegisterUser(BaseModel):
    username: str
    password: str

class ResponseModel(BaseModel):
    message: str