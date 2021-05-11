from typing import List

from pydantic import BaseModel

from todo_app.domain.todo import TodoEntity


class TodoBase(BaseModel):
    title: str


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True

    @classmethod
    def from_entity(cls, entity: TodoEntity):
        return cls(id=entity.id, title=entity.title, completed=entity.completed)


class PaginationResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_page: int
    has_next: bool


class TodoPaginationResponse(BaseModel):
    pagination: PaginationResponse
    data: List[Todo]


class TodoDetailResponse(BaseModel):
    data: Todo
