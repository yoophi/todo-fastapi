from typing import Optional, List

from fastapi import APIRouter
from fastapi import Depends, HTTPException

from todo_app.repositories.interface import IRepository
from todo_app.request_objects.todo_create import TodoCreateRequestObject
from todo_app.request_objects.todo_detail import TodoDetailRequestObject
from todo_app.request_objects.todo_list import TodoListRequestObject
from todo_app.request_objects.todo_update import TodoUpdateRequestObject
from todo_app.rest.utils import get_repository
from todo_app.schema import Todo, TodoCreate
from todo_app.use_cases.todo_create import TodoCreateUseCase
from todo_app.use_cases.todo_detail import TodoDetailUseCase
from todo_app.use_cases.todo_list import TodoListUseCase
from todo_app.use_cases.todo_update import TodoUpdateUseCase

router = APIRouter(prefix="/todos")


@router.get("/{todo_id}", response_model=Todo)
def todo_detail(todo_id: int, repository: IRepository = Depends(get_repository)):
    request_object = TodoDetailRequestObject.factory(todo_id=todo_id)

    uc = TodoDetailUseCase(repository)
    response = uc.execute(request_object)

    if not response:
        raise HTTPException(status_code=404, detail=response.message)

    todo = response.value
    return Todo(
        id=todo.id,
        title=todo.title,
        completed=todo.completed,
    )


@router.put("/{todo_id}", response_model=Todo)
def todo_update(todo_id: int, todo_in: TodoCreate, repository: IRepository = Depends(get_repository), ):
    request_objet = TodoUpdateRequestObject.factory(todo_id=todo_id, **todo_in.dict())

    uc = TodoUpdateUseCase(repository)
    response = uc.execute(request_objet)
    if not response:
        raise HTTPException(status_code=404, detail=response.message)

    todo = response.value
    return Todo(
        id=todo.id,
        title=todo.title,
        completed=todo.completed,
    )


@router.get("/", response_model=List[Todo])
def todo_list(limit: Optional[int] = 10, repository: IRepository = Depends(get_repository)):
    request_object = TodoListRequestObject.factory(limit=limit)

    uc = TodoListUseCase(repository)
    response = uc.execute(request_object)
    return [
        Todo(id=item.id, title=item.title, completed=item.completed)
        for item in response.value
    ]


@router.post("/", response_model=Todo)
def todo_add(item: TodoCreate, repository: IRepository = Depends(get_repository)):
    request_object = TodoCreateRequestObject.factory(title=item.title)

    uc = TodoCreateUseCase(repository)
    response = uc.execute(request_object)

    todo = response.value

    return Todo(id=todo.id, title=todo.title, completed=todo.completed)
