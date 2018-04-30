import TaskGateway
from models.Task import Task


class AddTaskInteractor:
    def __init__(self, task_gateway):
        self._task_gateway: TaskGateway = task_gateway

    def add_task(self, task_summary) -> str:
        new_task = Task("some id", task_summary)
        return self._task_gateway.save(new_task)
