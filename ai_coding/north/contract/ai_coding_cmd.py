from typing import Any
from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question: str


class ResponseModel(BaseModel):
    code: int
    message: Any