from typing import Optional, List

from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from todo_app.models import Todo as TodoModel
from todo_app.request_objects.todo_create import TodoCreateRequestObject
from todo_app.request_objects.todo_detail import TodoDetailRequestObject
from todo_app.request_objects.todo_list import TodoListRequestObject
from todo_app.request_objects.todo_update import TodoUpdateRequestObject
from todo_app.rest.utils import get_db
from todo_app.schema import Todo, TodoCreate

router = APIRouter(prefix='/todos')


@router.get("/{todo_id}", response_model=Todo)
def todo_detail(todo_id: int, db: Session = Depends(get_db)):
    request_object = TodoDetailRequestObject.factory(todo_id=todo_id)

    todo = db.query(TodoModel).get(request_object.todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail=f"Todo:{todo_id} not found")

    return todo


@router.put("/{todo_id}", response_model=Todo)
def todo_update(todo_id: int, todo_in: TodoCreate, db: Session = Depends(get_db)):
    request_objet = TodoUpdateRequestObject.factory(todo_id=todo_id, **todo_in.dict())

    todo = db.query(TodoModel).get(request_objet.todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail=f"Todo:{request_objet.todo_id} not found")

    if request_objet.title is not None:
        todo.title = request_objet.title
    if request_objet.completed is not None:
        todo.completed = request_objet.completed

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo


@router.get("/", response_model=List[Todo])
def todo_list(limit: Optional[int] = None, db: Session = Depends(get_db)):
    request_object = TodoListRequestObject.factory(
        limit=limit
    )
    todos = db.query(TodoModel).limit(request_object.limit).all()
    return todos


@router.post("/", response_model=Todo)
def todo_add(item: TodoCreate, db: Session = Depends(get_db)):
    request_object = TodoCreateRequestObject.factory(
        **item.dict()
    )

    todo = TodoModel(
        title=request_object.title,
        completed=request_object.completed,
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo
