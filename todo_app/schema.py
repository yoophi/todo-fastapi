from typing import Optional

from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    completed = bool

    class Config:
        orm_mode = True
