from typing import Callable
from fastapi import FastAPI, Request, Response
import uvicorn
import time

app = FastAPI()


@app.middleware("http")
async def my_middleware(request: Request, call_next: Callable):
    ip_address = request.client.host
    print(f"{ip_address=}")
    # if ip_address in ["127.0.0.1","localhost"]:
    #     return Response(status_code=429,content="Вы превысили количество запросов")
    start = time.perf_counter()
    response = await call_next(request)
    end = time.perf_counter() - start
    print(f"Время обработки запроса: {end}")
    response.headers["X-Special"] = "I am special"
    return response


@app.get("/users", tags=["Пользователи"])
async def get_users():
    time.sleep(0.5)
    return [{"id": 1, "name": "Vsevolod"}]


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
