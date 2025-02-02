from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def root():
    return "Главная страница"


@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"


@app.get("/user/{username}/{age}")
async def user_ident(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='Urban')],
        age: int = Path(ge=18, le=120, description='Enter age', example='25')) -> dict:
    # async def u_n(username: str, age: int) -> dict:
    return {"username": username, "age": age}


@app.get("/user/{item_id}")
# Пишет, что example устарел и нужно использовать examples. Но в swagger тогда не виден пример написания,
# со старой версией все впорядке
async def read_item(item_id: int = Path(ge=1, le=100, description='Enter User ID', example='25')):
    return f'Вы вошли как пользователь : {item_id}'
