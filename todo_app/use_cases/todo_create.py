from todo_app.repositories.interface import IRepository
from todo_app.repositories.sqla.models import Todo as TodoModel
from todo_app.response_objects import ResponseSuccess, ResponseFailure
from todo_app.request_objects.todo_create import TodoCreateRequestObject


class TodoCreateUseCase:
    repo: IRepository

    def __init__(self, repository: IRepository):
        self.repo = repository

    def execute(self, request_object: TodoCreateRequestObject):
        if not request_object:
            return ResponseFailure.build_from_invalid_request_object(
                invalid_request_object=request_object
            )

        todo = self.repo.create(
            title=request_object.title,
        )

        return ResponseSuccess(value=todo)
