from todo_app.request_objects.todo_paginate import TodoPaginateRequestObject


def test_factory():
    ro = TodoPaginateRequestObject.factory(pagination=0)
    assert bool(ro) is False, "limit 값은 0 보다 커야 한다."
