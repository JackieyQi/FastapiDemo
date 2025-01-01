#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
FastAPI 是一个现代、高性能的 Python Web 框架，
基于标准 Python 类型注释（type hints），
通过 ASGI（Asynchronous Server Gateway Interface）支持异步请求。
主要特点包括异步支持、自动生成文档、数据验证和自动序列化等。
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import test_time


app = FastAPI(title="FastAPIDemo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test_time.router, prefix="/api/test", tags=["demo_test"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, host="0.0.0.0", port=8080, reload=True)
