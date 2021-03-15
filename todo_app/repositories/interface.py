from abc import ABCMeta, abstractmethod


class IRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_todo_list(self, limit=10):
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
