from abc import abstractmethod
from typing import List

from models.Task import Task


class TaskGateway:

    @abstractmethod
    def save(self, task: Task) -> str:
        pass

    @abstractmethod
    def get_task(self, task_id: str):
        pass

    @abstractmethod
    def get_tasks(self) -> List[Task]:
        pass

    @abstractmethod
    def delete_task_by_id(self, task_id):
        pass
