from typing import Any
from pydantic import BaseModel


class ResponseModel(BaseModel):
    code: int
    message: Any
