from dataclasses import dataclass

from tests.request_objects import InvalidRequestObject


@dataclass
class TodoCreateRequestObject:
    title: str
    completed: bool = False

    @classmethod
    def factory(cls, title: str, ):
        invalid_ro = InvalidRequestObject()
        try:
            title = title.strip()
            if not title:
                return invalid_ro

            return cls(title=title, completed=False)
        finally:
            return invalid_ro
