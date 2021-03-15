import os

from todo_app.repositories.sqla.repo import SqlaRepository


def get_repository():
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_DATABASE = os.environ.get("DB_DATABASE")

    repository = SqlaRepository(
        connection_data={
            'user': DB_USER,
            'password': DB_PASSWORD,
            'host': DB_HOST,
            'port': DB_PORT,
            'database': DB_DATABASE,
        }
    )

    return repository
