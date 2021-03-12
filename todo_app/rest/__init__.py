from fastapi import FastAPI

from todo_app.rest.routers import todos


def create_app():
    app = FastAPI()

    app.include_router(todos.router)

    @app.get("/")
    def index():
        return "Hello, World!"

    return app
