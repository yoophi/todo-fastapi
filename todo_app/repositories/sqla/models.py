from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, Boolean

from todo_app.repositories.sqla.base import Base


@dataclass
class TodoEntity:
    id: int
    title: str
    completed: bool

    @classmethod
    def factory(cls, adict=None, **kwargs):
        if adict is None:
            adict = kwargs

        data = dict()
        data['id'] = adict.get('id')
        data['title'] = adict.get('title')
        data['completed'] = adict.get('completed')
        print(data)

        return cls(**data)


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(
        String(255),
    )
    completed = Column(Boolean, default=False)

    def to_entity(self):
        return TodoEntity.factory(
            id=self.id,
            title=self.title,
            completed=self.completed
        )
