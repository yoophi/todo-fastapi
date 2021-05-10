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
