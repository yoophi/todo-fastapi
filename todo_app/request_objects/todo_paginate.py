from dataclasses import dataclass

from todo_app.request_objects import InvalidRequestObject
from todo_app.request_objects.pagination import PaginationRequestObject


@dataclass
class TodoPaginateRequestObject:
    pagination: PaginationRequestObject

    @classmethod
    def factory(cls, pagination: PaginationRequestObject):
        invalid_ro = InvalidRequestObject()
        if not pagination:
            invalid_ro.add_error("pagination", "invalid pagination data")

            return invalid_ro

        return cls(pagination=pagination)
