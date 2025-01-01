#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker, declarative_base
from cached_property import threaded_cached_property


class Database(object):

    def demo_db(self):
        return create_engine(
            "postgresql://testdba:123456@127.0.0.1:5433/main",
            **{"pool_size": 10, "max_overflow": 10, "pool_timeout": 10, "pool_pre_ping": False, "echo": False}
        )

    @threaded_cached_property
    def async_engine(self):
        return create_async_engine(
            "postgresql+asyncpg://testdba:123456@127.0.0.1:5433/main",
            poolclass=QueuePool,
            **{"pool_size": 10, "max_overflow": 10, "pool_timeout": 10,
               "pool_recycle": 10, "pool_pre_ping": False, "echo": False}
        )

    @threaded_cached_property
    def session_factory(self):
        AsyncSessionLocal = sessionmaker(
            self.async_engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )
        return AsyncSessionLocal

    @threaded_cached_property
    async def get_session(self):
        async_session = self.session_factory
        try:
            yield async_session
        finally:
            await async_session.close()


db = Database()
Base = declarative_base()


async def get_db():
    async for session in db.get_session():
        yield session
