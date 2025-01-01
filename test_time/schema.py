#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
fastapi的主要特点
3.数据验证：
    数据验证和模型，
    FastAPI 中如何使用 Pydantic 验证请求数据？
        答：Pydantic 用于定义数据模型，通过声明一个 Pydantic BaseModel 子类，FastAPI 会自动验证和解析请求数据

    如何在 FastAPI 中实现请求和响应的模式转换？
        答：使用 Pydantic 模型不仅可以验证请求，还能作为响应模型，指定response_model来自动序列化输出数据并符合指定模式。
"""

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional


class Item(BaseModel):
    data: List[int]


class BannersDate(BaseModel):
    img_url: str
    html_url: str


class BannersResponse(BaseModel):
    data: List[BannersDate]


class UserBase(BaseModel):
    email: EmailStr
    name: str


class UserCreate(BaseModel):
    pass


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
