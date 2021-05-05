from dataclasses import dataclass

from todo_app.request_objects import ValidRequestObject, InvalidRequestObject


@dataclass
class PaginationRequestObject(ValidRequestObject):
    per_page: int
    page: int

    @classmethod
    def from_dict(cls, a_dict=None, **kwargs):
        if a_dict is None:
            a_dict = kwargs

        page = a_dict.get('page', 1)
        per_page = a_dict.get('per_page', 10)

        if not isinstance(page, int) or not isinstance(per_page, int):
            return InvalidRequestObject()

        return cls(page=page, per_page=per_page)
