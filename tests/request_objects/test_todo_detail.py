from todo_app.request_objects.todo_id import TodoIdRequestObject


def test_factory():
    ro = TodoIdRequestObject.factory(todo_id=0)
    assert bool(ro) is False, "todo_id 는 0 보다 커야 한다."
