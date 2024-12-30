# FastAPI Demo

## FastAPI框架的常见面试题

### 1. FastAPI基础概念：

* FastAPI 的主要特点是什么？
  * 答：FastAPI 是一个现代、高性能的 Python Web 框架，
  基于标准 Python 类型注释（type hints），通过 ASGI（Asynchronous Server Gateway Interface）支持异步请求。
  主要特点包括异步支持、自动生成文档、数据验证和自动序列化等。


* FastAPI 的异步特性是如何实现的？为什么它适合处理高并发请求？
  * 答：FastAPI 基于 Python 的 asyncio 和 async/await，允许非阻塞异步处理，使其适合高并发的应用场景，如聊天应用、I/O 密集型任务。



### 2. 路由和请求处理：

* 如何定义一个[路由](test_time/api.py?9)?
  ```python
  from fastapi import APIRouter
  router = APIRouter()
  ```



### 3. 数据验证和模型：

* FastAPI 中如何使用 Pydantic 验证请求数据？
  * 答：Pydantic 用于定义数据模型，通过声明一个 Pydantic BaseModel 子类，FastAPI 会自动验证和解析请求数据。
  [示例](test_time/schema.py):
  ```python
  from pydantic import BaseModel
  
  class Item(BaseModel):
    name: str
    price: float
    description: str = None
  
  @app.post("/items/")
  async def create_item(item: Item):
    return item
  ```


* 如何在 FastAPI 中实现请求和响应的模式转换？
  * 答：使用 Pydantic 模型不仅可以验证请求，还能作为响应模型，指定[response_model](test_time/api.py)来自动序列化输出数据并符合指定模式。



### 4. 异步处理和性能优化：
