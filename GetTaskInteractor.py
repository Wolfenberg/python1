import TaskGateway


class GetTaskInteractor:
    def __init__(self, task_gateway: TaskGateway):
        self._task_gateway = task_gateway

    def get_task(self, task_id: str):
        self._task_gateway.get_task(task_id)

    def get_tasks(self) -> []:
        return self._task_gateway.get_tasks()
