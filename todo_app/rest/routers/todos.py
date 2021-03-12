from typing import Optional, List

from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from todo_app.rest.utils import get_db
from todo_app.models import Todo as TodoModel
from todo_app.schema import Todo, TodoCreate

router = APIRouter(prefix='/todos')


@router.get("/{todo_id}", response_model=Todo)
def todo_detail(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail=f"Todo:{todo_id} not found")

    return todo


@router.put("/{todo_id}", response_model=Todo)
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


@router.get("/", response_model=List[Todo])
def todo_list(limit: Optional[int] = None, db: Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return todos


@router.post("/", response_model=Todo)
def todo_add(item: TodoCreate, db: Session = Depends(get_db)):
    todo = TodoModel(
        title=item.title,
        completed=item.completed,
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo
