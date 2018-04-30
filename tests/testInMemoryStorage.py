import unittest

from InMemoryStorage import InMemoryStorage
from models.Task import Task


class InMemoryStorageTest(unittest.TestCase):

    def test_saves_and_gets_task(self):
        sut = InMemoryStorage()
        task1 = Task("id1", "")
        task2 = Task("id2", "")
        task3 = Task("id3", "")

        sut.save(task1)
        sut.save(task2)
        sut.save(task3)

        self.assertEqual(sut.get_task("id2"), task2)

    def test_deletes_task(self):
        sut = InMemoryStorage()
        task1 = Task("id1", "")
        task2 = Task("id2", "")
        task3 = Task("id3", "")
        sut.save(task1)
        sut.save(task2)
        sut.save(task3)

        sut.delete_task_by_id("id2")

        self.assertEqual(sut.get_task("id2"), None)
