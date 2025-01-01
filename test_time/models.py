#! /usr/bin/env python
# -*- coding: UTF-8 -*-


from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from common.clients import Base


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, index=True)
    email = Column("email", String, unique=True, index=True)
    name = Column("name", String)
    created_at = Column("created_at", DateTime(timezone=True), server_default=func.now())
    updated_at = Column("updated_at", DateTime(timezone=True), onupdate=func.now())
