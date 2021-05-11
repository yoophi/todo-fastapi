from todo_app.repositories.interface import IRepository
from todo_app.request_objects.todo_id import TodoIdRequestObject
from todo_app.response_objects import ResponseFailure, ResponseSuccess


class TodoDeleteUseCase(object):
    repo: IRepository

    def __init__(self, repository: IRepository):
        self.repo = repository

    def execute(self, request_object: TodoIdRequestObject):
        todo_id = request_object.todo_id

        resp = self.repo.remove(todo_id)
        if resp is False:
            return ResponseFailure.build_resource_error(
                message=f"Delete failed: Todo:{todo_id}"
            )

        return ResponseSuccess(value=resp)
