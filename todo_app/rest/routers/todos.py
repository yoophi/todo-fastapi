from typing import Optional

from fastapi import APIRouter
from fastapi import Depends, HTTPException

from todo_app.repositories.interface import IRepository
from todo_app.request_objects.pagination import PaginationRequestObject
from todo_app.request_objects.todo_create import TodoCreateRequestObject
from todo_app.request_objects.todo_id import TodoIdRequestObject
from todo_app.request_objects.todo_paginate import TodoPaginateRequestObject
from todo_app.request_objects.todo_update import TodoUpdateRequestObject
from todo_app.rest.models import TodoPaginationResponse, TodoCreate, Todo, TodoDetailResponse, PaginationResponse
from todo_app.rest.utils import get_repository
from todo_app.use_cases.todo_create import TodoCreateUseCase
from todo_app.use_cases.todo_delete import TodoDeleteUseCase
from todo_app.use_cases.todo_detail import TodoDetailUseCase
from todo_app.use_cases.todo_list import TodoPagenateUseCase
from todo_app.use_cases.todo_update import TodoUpdateUseCase

router = APIRouter(prefix="/todos")


@router.get("/{todo_id}", response_model=TodoDetailResponse)
def todo_detail(todo_id: int, repository: IRepository = Depends(get_repository)):
    request_object = TodoIdRequestObject.factory(todo_id=todo_id)

    uc = TodoDetailUseCase(repository)
    response = uc.execute(request_object)

    if not response:
        raise HTTPException(status_code=404, detail=response.message)

    return TodoDetailResponse(data=Todo.from_entity(response.value))


@router.put("/{todo_id}", response_model=TodoDetailResponse)
def todo_update(
        todo_id: int,
        todo_in: TodoCreate,
        repository: IRepository = Depends(get_repository),
):
    request_objet = TodoUpdateRequestObject.factory(todo_id=todo_id, **todo_in.dict())

    uc = TodoUpdateUseCase(repository)
    response = uc.execute(request_objet)
    if not response:
        raise HTTPException(status_code=404, detail=response.message)

    return TodoDetailResponse(data=Todo.from_entity(response.value))


@router.delete("/{todo_id}")
def todo_delete(todo_id: int, repository: IRepository = Depends(get_repository)):
    request_object = TodoIdRequestObject.factory(todo_id=todo_id)

    uc = TodoDeleteUseCase(repository)
    response = uc.execute(request_object)

    if not response:
        raise HTTPException(status_code=404, detail=response.message)

    return {}


@router.get("/", response_model=TodoPaginationResponse)
def todo_paginate(
        page: Optional[int] = 1,
        per_page: Optional[int] = 10,
        repository: IRepository = Depends(get_repository)
):
    pagination = PaginationRequestObject.from_dict(
        page=page,
        per_page=per_page,
    )
    request_object = TodoPaginateRequestObject.factory(pagination=pagination)

    uc = TodoPagenateUseCase(repository)
    response = uc.execute(request_object)
    todos, pagination = response.value
    return TodoPaginationResponse(
        data=[
            Todo(id=item.id, title=item.title, completed=item.completed)
            for item in todos
        ],
        pagination=PaginationResponse(
            page=pagination.page,
            per_page=pagination.per_page,
            total=pagination.total,
            total_page=pagination.total_page,
            has_next=pagination.has_next,
        )
    )


@router.post("/", response_model=TodoDetailResponse)
def todo_add(item: TodoCreate, repository: IRepository = Depends(get_repository)):
    request_object = TodoCreateRequestObject.factory(title=item.title)

    uc = TodoCreateUseCase(repository)
    response = uc.execute(request_object)
    if not response:
        raise HTTPException(400)

    return TodoDetailResponse(data=Todo.from_entity(response.value))
