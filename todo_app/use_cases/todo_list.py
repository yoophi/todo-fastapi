from todo_app.models import Todo as TodoModel
from todo_app.response_objects import ResponseSuccess
from todo_app.request_objects.todo_list import TodoListRequestObject


class TodoListUseCase:
    def execute(self, request_object: TodoListRequestObject, db):
        todos = db.query(TodoModel).limit(request_object.limit).all()
        return ResponseSuccess(value=todos)
