from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, Возраст: 18'}


@app.get("/user")
async def unit() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def user_add(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='Urban')],
        age: int = Path(ge=18, le=120, description='Enter age', example='25')) -> str:
    index = len(users) + 1
    users[index] = f'Имя: {username}, Возраст: {age}'
    return f"User {index} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def user_update(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter ID', example='10')],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='Urban')],
        age: int = Path(ge=18, le=120, description='Enter age', example='25')) -> str:
    users[user_id] = f'Имя: {username}, Возраст: {age}'
    return f"User {user_id} is updated"


@app.delete("/user/{user_id}")
async def user_delete(user_id: int = Path(ge=1, le=100, description='Enter ID', example='10')) -> str:
    index = len(users)
    if user_id >= 1 and user_id <= index:
        users.pop(user_id)
        return f"User {user_id} is deleted"
    else:
        return f"Удаление невозможно введите индекс от 1 до {index}"
