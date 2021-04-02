from todo_app.repositories.interface import IRepository
from todo_app.repositories.sqla.models import Todo as TodoModel
from todo_app.response_objects import ResponseSuccess
from todo_app.request_objects.todo_list import TodoListRequestObject


class TodoListUseCase:
    repo: IRepository

    def __init__(self, repository: IRepository):
        self.repo = repository

    def execute(self, request_object: TodoListRequestObject):
        todos = self.repo.get_todo_list(limit=request_object.limit)

        return ResponseSuccess(value=todos)
