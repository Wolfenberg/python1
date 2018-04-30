from typing import List

from TaskGateway import TaskGateway
from models.Task import Task


class InMemoryStorage(TaskGateway):
    def __init__(self):
        self._tasks: List[Task] = []

    def save(self, task):
        task.id = len(self._tasks) + 1
        self._tasks.append(task)
        return task.id

    def get_task(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                return task

    def get_tasks(self) -> List[Task]:
        return self._tasks

    def delete_task_by_id(self, task_id):
        for t in self._tasks:
            if t.id == task_id:
                self._tasks.remove(t)
