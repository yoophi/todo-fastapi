from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Todo(BaseModel):
    id: int
    title: str
    completed: bool


@app.get('/')
def index():
    return "Hello, World!"


@app.get("/todos/{todo_id}")
def todo_detail(todo_id: int, ):
    return {"todo_id": todo_id, }


@app.put("/todos/{todo_id}")
def todo_update(todo_id: int, todo: Todo):
    return {"name": todo.title, "todo_id": todo_id}


@app.get("/todos")
def todo_list(limit: Optional[int] = None):
    return {"success": True}


@app.post("/todos")
def todo_add(item: Todo):
    print(item)
    return {"success": True}
