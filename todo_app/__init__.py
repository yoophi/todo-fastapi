from fastapi import FastAPI

from todo_app.database import SessionLocal
from todo_app.models import Todo as TodoModel
from todo_app.routers import todos
from todo_app.schema import Todo, TodoCreate

app = FastAPI()

app.include_router(todos.router)


@app.get("/")
def index():
    return "Hello, World!"
