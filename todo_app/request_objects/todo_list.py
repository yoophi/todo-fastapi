from dataclasses import dataclass

from todo_app.request_objects import InvalidRequestObject


@dataclass
class TodoListRequestObject:
    limit: int = 10

    @classmethod
    def factory(cls, limit: int = 10):
        invalid_ro = InvalidRequestObject()
        if not limit > 0:
            invalid_ro.add_error("limit", "limit should greater than 0")

            return invalid_ro

        return cls(limit=limit)
