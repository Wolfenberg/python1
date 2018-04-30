import TaskGateway


class DeleteTaskInteractor:
    def __init__(self, task_gateway: TaskGateway):
        self._task_gateway = task_gateway

    def delete_task(self, task_id):
        self._task_gateway.delete_task_by_id(task_id)
