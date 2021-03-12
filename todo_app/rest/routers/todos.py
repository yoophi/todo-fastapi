from typing import Optional, List

from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from todo_app.request_objects.todo_create import TodoCreateRequestObject
from todo_app.request_objects.todo_detail import TodoDetailRequestObject
from todo_app.request_objects.todo_list import TodoListRequestObject
from todo_app.request_objects.todo_update import TodoUpdateRequestObject
from todo_app.rest.utils import get_db
from todo_app.schema import Todo, TodoCreate
from todo_app.use_cases.todo_create import TodoCreateUseCase
from todo_app.use_cases.todo_detail import TodoDetailUseCase
from todo_app.use_cases.todo_list import TodoListUseCase
from todo_app.use_cases.todo_update import TodoUpdateUseCase

router = APIRouter(prefix="/todos")


@router.get("/{todo_id}", response_model=Todo)
def todo_detail(todo_id: int, db: Session = Depends(get_db)):
    request_object = TodoDetailRequestObject.factory(todo_id=todo_id)

    uc = TodoDetailUseCase()
    response = uc.execute(request_object, db)

    if not response:
        raise HTTPException(status_code=404, detail=response.message)

    return response.value


@router.put("/{todo_id}", response_model=Todo)
def todo_update(todo_id: int, todo_in: TodoCreate, db: Session = Depends(get_db)):
    request_objet = TodoUpdateRequestObject.factory(todo_id=todo_id, **todo_in.dict())

    uc = TodoUpdateUseCase()
    response = uc.execute(request_objet, db)
    if not response:
        raise HTTPException(status_code=404, detail=response.message)

    return response.value


@router.get("/", response_model=List[Todo])
def todo_list(limit: Optional[int] = None, db: Session = Depends(get_db)):
    request_object = TodoListRequestObject.factory(limit=limit)

    uc = TodoListUseCase()
    response = uc.execute(request_object, db)
    return response.value


@router.post("/", response_model=Todo)
def todo_add(item: TodoCreate, db: Session = Depends(get_db)):
    print("=== item ===")
    print(item)
    request_object = TodoCreateRequestObject.factory(title=item.title)
    print("type(request_object)", type(request_object))
    print("request_object", request_object)

    uc = TodoCreateUseCase()
    response = uc.execute(request_object, db)

    return response.value
