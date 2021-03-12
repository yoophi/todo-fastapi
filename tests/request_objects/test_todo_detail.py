from todo_app.request_objects.todo_detail import TodoDetailRequestObject


def test_factory():
    ro = TodoDetailRequestObject.factory(todo_id=0)
    assert bool(ro) is False, \
        "todo_id 는 0 보다 커야 한다."
