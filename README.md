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

* 如何在 FastAPI 中实现异步数据库查询？
  * 答：在数据库查询中使用支持异步的 ORM（如 [SQLAlchemy 的异步扩展](common/clients.py)），并在函数中使用 await 进行异步查询处理。


* 如何优化 FastAPI 的性能？
  * 答：可以通过使用异步编程、缓存、数据库连接池、内容压缩和合理的响应模式等手段提升性能。
  此外，使用 FastAPI 时还可以配合 [Uvicorn 和 Gunicorn 等 ASGI 服务器](app.py)。



### 5. 中间件和依赖注入:

* 如何在 FastAPI 中添加全局中间件？
  * 答：可以使用 [add_middleware](app.py) 方法来添加中间件。


* FastAPI 的依赖注入系统是如何工作的？
  * 答：FastAPI 的依赖注入通过 Depends 实现，将参数作为函数的依赖项，便于重用。
  例如，[数据库会话](test_time/api.py)、用户认证等可作为依赖注入，避免在各路由中重复创建。



### 6. 认证与授权:

* 如何在 FastAPI 中实现用户认证？
  * 答：FastAPI 支持 OAuth2 和 JSON Web Token (JWT) 认证，可以通过 OAuth2PasswordBearer 依赖和 JWT 来实现身份验证。


* JWT 认证在 FastAPI 中的基本实现步骤有哪些？
  * 答：1) 定义 secret_key 和算法；2) 生成 JWT token；3) 创建认证依赖，校验用户凭证和 token 是否有效。



### 7. 错误处理与测试:

* 何在 FastAPI 中处理全局异常？
  * 答：可以使用 @app.exception_handler 装饰器来定义自定义的异常处理函数。


* 如何编写 FastAPI 应用的测试？
  * 答：可以使用 FastAPI 提供的 TestClient，并结合 pytest 来编写测试。例如：
  ```python
  from fastapi.testclient import TestClient

  client = TestClient(app)

  def test_read_item():
      response = client.get("/items/1")
      assert response.status_code == 200
      assert response.json() == {"item_id": 1}
  ```


### 8.  自动生成文档:

* FastAPI 使用了哪些工具来生成文档？
  * 答：FastAPI 使用 OpenAPI 生成 Swagger 文档，并支持 ReDoc 文档。
  启动应用后，可以访问 /docs（Swagger）或 /redoc 查看自动生成的 API 文档。

