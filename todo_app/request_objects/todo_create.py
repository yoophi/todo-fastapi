from dataclasses import dataclass

from todo_app.request_objects import InvalidRequestObject


@dataclass
class TodoCreateRequestObject:
    title: str

    @classmethod
    def factory(
        cls,
        title: str,
    ):
        invalid_request_object = InvalidRequestObject()

        try:
            title = title.strip()
            if not title:
                return invalid_request_object

            return cls(title=title)
        except Exception as e:
            return invalid_request_object
