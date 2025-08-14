from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/users")
async def get_users():
    ...
    return [{"id": 1, "name": "Vsevolod"}]

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=8000)

# запускаем командой
#
# docker run --name=my_first_container -p 1253:8000 my_first_image