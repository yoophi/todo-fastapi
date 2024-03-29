from todo_app.repositories.interface import IRepository
from todo_app.request_objects.todo_id import TodoIdRequestObject
from todo_app.response_objects import ResponseFailure, ResponseSuccess


class TodoDetailUseCase(object):
    repo: IRepository

    def __init__(self, repository: IRepository):
        self.repo = repository

    def execute(self, request_object: TodoIdRequestObject):
        todo_id = request_object.todo_id

        todo = self.repo.get(todo_id)
        if todo is None:
            return ResponseFailure.build_resource_error(
                message=f"Todo:{todo_id} not found."
            )

        return ResponseSuccess(value=todo)
