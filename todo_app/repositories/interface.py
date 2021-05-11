from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class PaginationDto:
    page: int
    per_page: int


@dataclass
class PaginationResponse:
    page: int
    per_page: int
    total: int
    total_page: int

    @property
    def has_next(self):
        return self.total_page > self.page


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
    def list(self, limit=10):
        pass

    @abstractmethod
    def paginate(
            self,
            pagination: PaginationDto,
    ):
        pass

    @abstractmethod
    def get(self, id_):
        pass

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def update(self, id_, **kwargs):
        pass

    @abstractmethod
    def remove(self, id_):
        pass
