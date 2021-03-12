from typing import Optional, List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from todo_app.database import SessionLocal
from todo_app.models import Todo as TodoModel
from todo_app.schema import Todo, TodoCreate

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return "Hello, World!"


@app.get("/todos/{todo_id}", response_model=Todo)
def todo_detail(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail=f"Todo:{todo_id} not found")

    return todo


@app.put("/todos/{todo_id}", response_model=Todo)
def todo_update(todo_id: int, todo_in: TodoCreate, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail=f"Todo:{todo_id} not found")

    todo.title = todo_in.title
    todo.completed = todo_in.completed
    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo


@app.get("/todos", response_model=List[Todo])
def todo_list(limit: Optional[int] = None, db: Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return todos


@app.post("/todos", response_model=Todo)
def todo_add(item: TodoCreate, db: Session = Depends(get_db)):
    todo = TodoModel(
        title=item.title,
        completed=item.completed,
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo
