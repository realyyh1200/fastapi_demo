from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import async_sessionmaker

from settings import ASYNC_DATABASE_URL, DATABASE_URL
from logger import logger

# 同步数据库连接
engine = create_engine(DATABASE_URL)

LocalSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


@contextmanager
def get_db():
    session = LocalSession()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error(f"数据库事务失败: {e}")
        raise
    finally:
        session.close()


# 异步数据库连接,用于处理高并发，IO密集型等场景
async_engine = create_async_engine(ASYNC_DATABASE_URL)

LocalAsyncSession = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=True  # 为了保证强一致性，设置为True
)


BaseTable = declarative_base()


async def get_async_db():
    async with LocalAsyncSession() as session:
        yield session
