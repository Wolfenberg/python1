import unittest
from AddTaskInteractor import AddTaskInteractor
from tests.TaskGatewaySpy import TaskGatewaySpy


class AddTaskInteractorTests(unittest.TestCase):

    def test_add_task(self):
        task_gateway = TaskGatewaySpy()
        sut = AddTaskInteractor(task_gateway)

        sut.add_task("task summary")

        self.assertEqual("task summary", task_gateway.saved_task.summary)
