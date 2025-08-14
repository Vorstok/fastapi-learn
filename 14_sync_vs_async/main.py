from fastapi import FastAPI, Query, Body
from fastapi.openapi.docs import get_swagger_ui_html
import uvicorn

app = FastAPI(docs_url=None)

hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"},
]

import time
import asyncio
import threading


@app.get("/sync/{id}")
def sync_func(id: int):
    print(f"sync. Потоков: {threading.active_count()}")

    timer = time.time()
    print(f"sync. Начал {id}")
    time.sleep(3)
    print(f"sync. Закончил {id}: {time.time() - timer:.2f}")


@app.get("/async/{id}")
async def async_func(id: int):
    print(f"async. Потоков: {threading.active_count()}")
    timer = time.time()
    print(f"async. Начал {id}")
    await asyncio.sleep(3)
    print(f"async. Закончил {id}: {time.time() - timer:.2f}")


@app.get("/hotels")
def get_hotels(
        id: int | None = Query(None, description="Айдишник"),
        title: str | None = Query(None, description="Название отеля"),
):
    hotels_ = []
    for hotel in hotels:
        if id and hotel["id"] != id:
            continue
        if title and hotel["title"] != title:
            continue
        hotels_.append(hotel)
    return hotels


@app.post("/hotels")
def create_hotel(
        title: str = Body(embed=True)
):
    global hotels
    hotels.append({
        "id": hotels[-1]["id"] + 1,
        "title": title
    })
    return {"status": "OK"}


@app.put("hotels/{hotel_id}")
def edit_hotel(
        hotel_id: int,
        title: str = Body(),
        name: str = Body(),
):
    global hotels
    hotel = [hotel for hotel in hotels if hotel["id"] == hotel_id][0]
    hotel["title"] = title
    hotel[name] = name
    return {"status": "OK"}


@app.patch(
    "/hotels/{hotel_id}",
    summary="Частичное обновление данных об отеле",
    description="<h1>Тут мы частично обновляем данные об отеле: можно отправить name, а можно title</h1>",
)
def partially_edi_hotel(
        hotel_id: int,
        title: str | None = Body(None),
        name: str | None = Body(None),
):
    global hotels
    hotel = [hotel for hotel in hotels if hotel["id"] == hotel_id][0]
    if title:
        hotel["title"] = title
    if name:
        hotel["name"] = name
    return {"status": "OK"}


@app.delete("/hotels/{hotel_id}")
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] == hotel_id]
    return {"status": "OK"}


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(): ...


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
