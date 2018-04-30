import unittest

from GetTaskInteractor import GetTaskInteractor
from tests.TaskGatewaySpy import TaskGatewaySpy


class GetTaskInteractorTests(unittest.TestCase):

    def test_gets_task_by_id(self):
        task_gateway = TaskGatewaySpy()
        sut = GetTaskInteractor(task_gateway)

        sut.get_task("task id")

        self.assertEqual(task_gateway.used_get_task_id, "task id")

    def test_gets_all_tasks(self):
        task_gateway = TaskGatewaySpy()
        sut = GetTaskInteractor(task_gateway)

        tasks: [] = sut.get_tasks()

        self.assertEqual(len(tasks), 1)
