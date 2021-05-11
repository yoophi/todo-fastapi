from todo_app.repositories.interface import IRepository
from todo_app.repositories.sqla.models import Todo as TodoModel
from todo_app.response_objects import ResponseFailure, ResponseSuccess
from todo_app.request_objects.todo_update import TodoUpdateRequestObject


class TodoUpdateUseCase:
    repo: IRepository

    def __init__(self, repository: IRepository):
        self.repo = repository

    def execute(self, request_objet: TodoUpdateRequestObject):
        todo_id = request_objet.todo_id
        title = request_objet.title
        completed = request_objet.completed

        todo = self.repo.update(todo_id, title=title, completed=completed)
        if todo is None:
            return ResponseFailure.build_resource_error(
                message=f"Todo:{todo_id} not found"
            )

        return ResponseSuccess(value=todo)
