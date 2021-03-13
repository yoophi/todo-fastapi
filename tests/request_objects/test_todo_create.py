from todo_app.request_objects.todo_create import TodoCreateRequestObject


def test_factory():
    for title in (None, " ", ""):
        ro = TodoCreateRequestObject.factory(title=title)
        assert bool(ro) is False, "title 값은 빈 값 또는 None 이 아니어야 한다."


def test_valid_ro():
    for title in ("valid-title",):
        ro = TodoCreateRequestObject.factory(title=title)
        ro1 = TodoCreateRequestObject(title="hello")
        assert bool(ro1) is True
        print(type(ro))
        assert bool(ro) is True, "title 비어있지 않을 때 정상 request_object 가 생성되어야 한다."
