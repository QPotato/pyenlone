import unittest
from datetime import datetime

from pyenlone import Tasks, OpType, TaskType

class TestTasks(unittest.TestCase):
    def setUp(self):
        with open("APIKEY") as input_file:
            apikey = input_file.read()[:-1]
        self.tasks_api = Tasks(apikey=apikey, realtime=True)
        self.test_op = self.tasks_api.new_operation("Test OP", OpType.FIELD)

    def tearDown(self):
        self.test_op.delete()

    def test_op(self):
        print(self.test_op.id)
        self.test_op.name = "name change test"
        print(self.test_op.name)
        print(self.test_op.owner)
        self.test_op.start = datetime.now()
        print(self.test_op.start)
        self.test_op.end = datetime.now()
        print(self.test_op.end)
        print(self.test_op.type)
        # ...
    def test_task(self):
        task = self.test_op.new_task(-32.878981, -61.022595, TaskType.DESTROY)
        task = self.test_op.new_task(TaskType.LINK, link_target)
