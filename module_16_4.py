# Задача "Модель пользователя"
from gc import enable

from fastapi import FastAPI, HTTPException
from typing import List, Annotated
from pydantic import BaseModel, Field

app = FastAPI()

users = []


class User(BaseModel):
    id: int = Field(1, ge=1, le=100)
    username: str = Field(..., min_length=2, max_length=50, description='Имя пользователя')
    age: int = Field(16, ge=16, le=80, description='Возраст пользователя')


@app.get("/users", response_model=List[User])
async def GetUser():
    return users


@app.post("/users", response_model=User)
async def AddUser(user: User):
    new_id = max((t.id for t in users), default=0) + 1
    new_user = User(id=new_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user


@app.put("/users/{id}", response_model=User)
async def UpdateUser(id: int, user: User):
    for i in users:
        if i.id == id:
            i.username = user.username
            i.age = user.age
            return i
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/users/{id}", response_model=User)
async def DelUser(id: int, user: User):
    for i, t in enumerate(users):
        if t.id == id:
            del users[i]
            return user
    raise HTTPException(status_code=404, detail="User was not found")
