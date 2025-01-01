#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import time
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from common.clients import get_db
from .router import router
from .schema import BannersResponse, BannersDate, Item, UserResponse, UserCreate
from .models import User


@router.get("/get_time", response_model=BannersResponse, summary="查询时间")
def get_time(name: str):
    # return f"{name}: {time.ctime()}"
    return BannersResponse(data=[
        BannersDate(img_url=str(time.ctime()), html_url=str(time.time())),
        ])


@router.post("/get_time", summary="查询时间")
def get_time(item: Item):
    result = []
    for i in item.data:
        result.append(time.ctime(i))
    return result


@router.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        db_user = User(email=user.email, name=user.name)
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

