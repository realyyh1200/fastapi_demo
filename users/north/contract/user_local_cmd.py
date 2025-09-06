from pydantic import BaseModel


class RegisterUserCmd(BaseModel):
    user_name: str
    password: str

    def __str__(self):
        return f"RegisterUserCmd(user_name={self.user_name}, password=***)"

class LoginUserCmd(BaseModel):
    user_name: str
    password: str

    def __str__(self):
        return f"LoginUserCmd(user_name={self.user_name}, password=***)"

class ResponseModel(BaseModel):
    code: int
    message: str
