# 用于BaseTable与BaseModel之间的转换
from typing import Optional
from datetime import datetime


def to_model(sqlalchemy_model, pydantic_model):
    data = {}
    for field_name in pydantic_model.model_fields:
        if hasattr(sqlalchemy_model, field_name):
            sqlalchemy_value = getattr(sqlalchemy_model, field_name)
            # 获取 Pydantic 模型字段的类型
            pydantic_type = pydantic_model.model_fields[field_name].annotation
            data[field_name] = sqlalchemy_value
            if (pydantic_type == str or pydantic_type == Optional[str]) and isinstance(sqlalchemy_value, int):
                data[field_name] = str(sqlalchemy_value)
            elif (pydantic_type == str or pydantic_type == Optional[str]) and isinstance(sqlalchemy_value, datetime):
                data[field_name] = sqlalchemy_value.strftime("%Y-%m-%d %H:%M:%S") if sqlalchemy_value else None
            else:
                data[field_name] = sqlalchemy_value
    return pydantic_model.model_validate(data)
