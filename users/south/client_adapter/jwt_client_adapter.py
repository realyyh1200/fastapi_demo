from datetime import datetime, timedelta, timezone

import jwt
from fastapi import HTTPException, status
from logger import logger
from settings import SECRET_KEY, ACCESS_TOKEN_EXPIRE_DAYS, ALGORITHM
from ...domain.port.client.jwt_client import JWTClient


class JWTClientAdapter(JWTClient):
    def create_token(self, user_name: str) -> str:
        payload = {
            'username': user_name,
            'exp': datetime.now(timezone.utc) + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS),
            'iat': datetime.now(timezone.utc)  # 签发时间
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return token

    def verify_token(self, token: str) -> str | None:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload.get('username', None)
        except jwt.ExpiredSignatureError:
            logger.error('expired token')
            return None
        except jwt.InvalidTokenError:
            logger.error('invalid token')
            return None

    def get_current_user(self, token: str) -> str:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        user_name = self.verify_token(token)
        if user_name is None:
            raise credentials_exception
        return user_name
