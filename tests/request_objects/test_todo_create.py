from todo_app.request_objects.todo_create import TodoCreateRequestObject


def test_factory():
    for title in (None, " ", ""):
        ro = TodoCreateRequestObject.factory(
            title=title
        )
        assert bool(ro) is False, "title 값은 빈 값 또는 None 이 아니어야 한다."
