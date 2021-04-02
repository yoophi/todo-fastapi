from fastapi import FastAPI, Depends

from todo_app.rest.routers import todos
from todo_app.rest.settings import SettingsInterface, get_settings


def create_app():
    app = FastAPI()

    app.include_router(todos.router)

    @app.get("/")
    def index():
        return "Hello, World!"

    @app.get("/config")
    async def dump_config(settings: SettingsInterface = Depends(get_settings)):
        if settings.debug:
            return settings

        return {}

    return app
