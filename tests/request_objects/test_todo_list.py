from todo_app.request_objects.todo_list import TodoListRequestObject


def test_factory():
    ro = TodoListRequestObject.factory(limit=0)
    assert bool(ro) is False, "limit 값은 0 보다 커야 한다."
