import math
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from todo_app.repositories.interface import IRepository, PaginationDto, PaginationResponse
from todo_app.repositories.sqla.base import Base
from todo_app.repositories.sqla.models import Todo


class TodoSqlaRepository(IRepository):
    def __init__(self, db=None, connection_data=None):
        self.db = db
        self.cls = Todo

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

    def list(self, limit=10):
        with self.session_context() as session:
            items = session.query(self.cls).limit(limit).all()

        return [item.to_entity() for item in items]

    def paginate(
            self,
            pagination: PaginationDto,
    ):
        page = pagination.page
        per_page = pagination.per_page
        offset = (page - 1) * per_page

        with self.session_context() as session:
            query = session.query(self.cls)
            total = query.count()
            total_page = math.ceil(total / per_page)
            items = query.limit(per_page).offset(offset)
            pagination = PaginationResponse(
                page=page,
                per_page=per_page,
                total=total,
                total_page=total_page,
            )

        return [item.to_entity() for item in items], pagination

    def get(self, id_):
        with self.session_context() as session:
            item = session.query(self.cls).get(id_)
            if not item:
                return None

        return item.to_entity()

    def create(self, **kwargs):
        with self.session_context() as session:
            data = dict(kwargs, completed=False)
            item = self.cls(**data)
            session.add(item)
            session.commit()
            session.refresh(item)

        return item.to_entity()

    def update(self, id_, **kwargs):
        with self.session_context() as session:
            item = session.query(self.cls).get(id_)
            if not item:
                return None

            if kwargs.get('title') is not None:
                item.title = kwargs.get('title')
            if kwargs.get('completed') is not None:
                item.completed = kwargs.get('completed')

            session.add(item)
            session.commit()
            session.refresh(item)

        return item.to_entity()

    def remove(self, id_):
        with self.session_context() as session:
            item = session.query(self.cls).get(id_)
            if not item:
                return False

            session.delete(item)
            session.commit()
            return True
