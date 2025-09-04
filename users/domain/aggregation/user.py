import string
from pydantic import BaseModel, Field, field_validator, ValidationError


class User(BaseModel):
    name: str = Field(...,max_length=49)
    password: str = Field(...,min_length=8)

    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        has_letter = any(c.isalpha() for c in v)
        has_digit = any(c.isdigit() for c in v)
        has_special = any(c in string.punctuation for c in v)
        if not (has_letter and has_digit and has_special):
            raise ValidationError('密码必须包含英文、数字与特殊符号')
        return v