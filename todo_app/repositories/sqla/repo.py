from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from todo_app.repositories.interface import IRepository
from todo_app.repositories.sqla.base import Base
from todo_app.repositories.sqla.models import Todo


class SqlaRepository(IRepository):
    def __init__(self, db=None, connection_data=None):
        self.db = db
        if db is None:
            db_user = connection_data.get("user")
            db_password = connection_data.get("password")
            db_host = connection_data.get("host")
            db_port = connection_data.get("port")
            db_database = connection_data.get("database")
            dsn = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}"
            self.engine = create_engine(dsn)
            Base.metadata.bind = self.engine

    @property
    def session_context(self):
        if self.db:

            @contextmanager
            def session_scope():
                yield self.db.session

        else:

            @contextmanager
            def session_scope():
                session_local = sessionmaker(bind=self.engine)
                session = session_local()
                try:
                    yield session
                finally:
                    session.close()

        return session_scope

    def get_todo_list(self, limit=10):
        with self.session_context() as session:
            todos = session.query(Todo).limit(limit).all()

        return [todo.to_entity() for todo in todos]

    def get_todo(self, todo_id):
        with self.session_context() as session:
            todo = session.query(Todo).get(todo_id)
            if not todo:
                return None

        return todo.to_entity()

    def create_todo(self, title):
        with self.session_context() as session:
            todo = Todo(
                title=title,
                completed=False,
            )
            session.add(todo)
            session.commit()
            session.refresh(todo)

        return todo.to_entity()

    def update_todo(self, todo_id, title, completed):
        with self.session_context() as session:
            todo = session.query(Todo).get(todo_id)
            if not todo:
                return None

            if title is not None:
                todo.title = title
            if completed is not None:
                todo.completed = completed

            session.add(todo)
            session.commit()
            session.refresh(todo)

        return todo.to_entity()

    def remove_todo(self):
        pass
