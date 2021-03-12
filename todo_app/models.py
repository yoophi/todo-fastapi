from sqlalchemy import Column, Integer, String, Boolean

from todo_app.database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(
        String(255),
    )
    completed = Column(Boolean, default=False)
