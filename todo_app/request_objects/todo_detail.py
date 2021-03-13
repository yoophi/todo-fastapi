from dataclasses import dataclass

from todo_app.request_objects import InvalidRequestObject


@dataclass
class TodoDetailRequestObject:
    todo_id: int

    @classmethod
    def factory(cls, todo_id: int):
        invalid_request_object = InvalidRequestObject()
        if todo_id < 1:
            return invalid_request_object

        return cls(
            todo_id=todo_id,
        )
