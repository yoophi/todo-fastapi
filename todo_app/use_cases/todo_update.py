from todo_app.models import Todo as TodoModel
from todo_app.response_objects import ResponseFailure, ResponseSuccess
from todo_app.request_objects.todo_update import TodoUpdateRequestObject


class TodoUpdateUseCase:
    def execute(self, request_objet: TodoUpdateRequestObject, db):
        todo = db.query(TodoModel).get(request_objet.todo_id)
        if not todo:
            return ResponseFailure.build_resource_error(
                message=f"Todo:{request_objet.todo_id} not found"
            )

        if request_objet.title is not None:
            todo.title = request_objet.title
        if request_objet.completed is not None:
            todo.completed = request_objet.completed

        db.add(todo)
        db.commit()
        db.refresh(todo)

        return ResponseSuccess(value=todo)
