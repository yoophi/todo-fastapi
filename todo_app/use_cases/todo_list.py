from todo_app.repositories.interface import IRepository, PaginationDto
from todo_app.repositories.sqla.models import Todo as TodoModel
from todo_app.response_objects import ResponseSuccess, ResponseFailure
from todo_app.request_objects.todo_paginate import TodoPaginateRequestObject


class TodoPagenateUseCase:
    repo: IRepository

    def __init__(self, repository: IRepository):
        self.repo = repository

    def execute(self, request_object: TodoPaginateRequestObject):
        if not request_object:
            return ResponseFailure.build_from_invalid_request_object(request_object)

        pagination = PaginationDto(
            page=request_object.pagination.page,
            per_page=request_object.pagination.per_page,
        )
        todos, pagination = self.repo.paginate(pagination=pagination)

        return ResponseSuccess(value=(todos, pagination))
