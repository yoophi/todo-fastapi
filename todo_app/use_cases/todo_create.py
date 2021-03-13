from todo_app.models import Todo as TodoModel
from todo_app.response_objects import ResponseSuccess, ResponseFailure
from todo_app.request_objects.todo_create import TodoCreateRequestObject


class TodoCreateUseCase:
    def execute(self, request_object: TodoCreateRequestObject, db):
        if not request_object:
            return ResponseFailure.build_from_invalid_request_object(
                invalid_request_object=request_object
            )

        todo = TodoModel(
            title=request_object.title,
            completed=False,
        )
        db.add(todo)
        db.commit()
        db.refresh(todo)

        return ResponseSuccess(value=todo)
