from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Главная страница"


@app.get("/user")
async def u_n(username: str = "Unit", age: int = 16) -> dict:
    # async def u_n(username: str, age: int) -> dict:
    return {"username": username, "age": age}


@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"


@app.get("/user/{item_id}")
async def read_item(item_id: int):
    return f'Вы вошли как пользователь : {item_id}'
