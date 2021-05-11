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

        data = {key: adict.get(key) for key in ("id", "title", "completed")}

        return cls(**data)
