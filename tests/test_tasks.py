import unittest
from datetime import datetime

from pyenlone import Tasks, OpType, TaskType

DRAW = """[{"type":"polyline","latLngs":[{"lat":-32.777775,"lng":-61.604255},{"lat":-33.258328,"lng":-58.023684}],"color":"#a24ac3"}]"""

class TestTasks(unittest.TestCase):
    def setUp(self):
        with open("APIKEY") as input_file:
            apikey = input_file.read()[:-1]
        self.tasks_api = Tasks(apikey=apikey)

    def tearDown(self):
        self.test_op.delete()

    def test_op(self):
        T = self.tasks_api
        op = T.new_operation("Test OP", OpType.FIELD, draw=DRAW)
        op.
        print(T.get_op(op.op_id))
        print(T.get_ops())
        print(T.post_op())

    def test_task(self):
        task = self.test_op.new_task(-32.878981, -61.022595, TaskType.DESTROY)
