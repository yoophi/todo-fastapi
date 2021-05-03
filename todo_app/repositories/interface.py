from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class PaginationDto:
    page: int
    per_page: int


@dataclass
class PaginationFilterDto:
    key: str
    value: str


@dataclass
class PaginationSortDto:
    key: str
    descending: bool


class IRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_todo_list(self, limit=10):
        pass

    @abstractmethod
    def get_todo_paginate(
        self,
        pagination: PaginationDto,
        filters: List[PaginationFilterDto],
        sort: Optional[PaginationSortDto] = None,
    ):
        pass

    @abstractmethod
    def get_todo(self, todo_id):
        pass

    @abstractmethod
    def create_todo(self, title):
        pass

    @abstractmethod
    def update_todo(self, todo_id, title, completed):
        pass

    @abstractmethod
    def remove_todo(self):
        pass
