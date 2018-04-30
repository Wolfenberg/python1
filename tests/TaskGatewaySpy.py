from TaskGateway import TaskGateway
from models.Task import Task


class TaskGatewaySpy(TaskGateway):

    def __init__(self):
        self.saved_task = None
        self.used_get_task_id = None
        self.is_get_tasks_called = False

    def save(self, task):
        self.saved_task = task

    def get_task(self, task_id):
        self.used_get_task_id = task_id
        super().get_task(task_id)

    def get_tasks(self):
        return [Task("id", "summary")]
