from sqlalchemy import Column, Integer, String, Boolean

from todo_app.domain.todo import TodoEntity
from todo_app.repositories.sqla.base import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(
        String(255),
    )
    completed = Column(Boolean, default=False)

    def to_entity(self):
        return TodoEntity.factory(
            id=self.id, title=self.title, completed=self.completed
        )
