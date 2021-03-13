from dataclasses import dataclass
from typing import Optional

from todo_app.request_objects import InvalidRequestObject


@dataclass
class TodoUpdateRequestObject:
    todo_id: int
    title: Optional[str]
    completed: Optional[bool]

    @classmethod
    def factory(
        cls, todo_id: int, title: Optional[str] = None, completed: Optional[bool] = None
    ):

        return cls(todo_id=todo_id, title=title, completed=completed)
