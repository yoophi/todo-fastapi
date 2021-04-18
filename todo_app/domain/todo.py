from dataclasses import dataclass


@dataclass
class TodoEntity:
    id: int
    title: str
    completed: bool

    @classmethod
    def factory(cls, adict=None, **kwargs):
        if adict is None:
            adict = kwargs

        data = dict()
        data["id"] = adict.get("id")
        data["title"] = adict.get("title")
        data["completed"] = adict.get("completed")

        return cls(**data)
