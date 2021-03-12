from todo_app.request_objects.todo_update import TodoUpdateRequestObject


def test_todo_update_ro_is_valid():
    ro_with_empty_completed = TodoUpdateRequestObject.factory(
        todo_id=1, title="sample text", completed=None)

    assert bool(ro_with_empty_completed) is True, "completed 값은 None 일 수 있다."

    ro_with_empty_title = TodoUpdateRequestObject.factory(
        todo_id=1, title=None, completed=True)

    assert bool(ro_with_empty_title) is True, "title 값은 None 일 수 있다."
