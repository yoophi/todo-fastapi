from todo_app.models import Todo as TodoModel
from todo_app.response_objects import ResponseFailure, ResponseSuccess
from todo_app.request_objects.todo_detail import TodoDetailRequestObject


class TodoDetailUseCase(object):
    def execute(self, request_object: TodoDetailRequestObject, db):
        todo = db.query(TodoModel).get(request_object.todo_id)
        if not todo:
            return ResponseFailure.build_resource_error(
                message=f"Todo:{request_object.todo_id} not found"
            )

        return ResponseSuccess(value=todo)
