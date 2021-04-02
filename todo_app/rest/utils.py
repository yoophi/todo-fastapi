from fastapi import Depends

from todo_app.repositories.sqla.repo import SqlaRepository
from todo_app.rest.settings import SettingsInterface, get_settings


def get_repository(settings: SettingsInterface = Depends(get_settings)):
    return SqlaRepository(
        connection_data={
            'user': settings.db_user,
            'password': settings.db_password,
            'host': settings.db_host,
            'port': settings.db_port,
            'database': settings.db_database,
        }
    )
