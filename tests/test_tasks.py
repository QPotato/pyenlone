import unittest
from datetime import datetime

from pyenlone.tasks import Tasks, OpType, TaskType

DRAW = """[{"type":"polyline","latLngs":[{"lat":-32.777775,"lng":-61.604255},{"lat":-33.258328,"lng":-58.023684}],"color":"#a24ac3"}]"""

def print_op(op):
    print(op.id)
    print(op.name)
    print(op.owner)
    print(op.start)
    print(op.end)
    print(op.type)
    print(op.agentDraw)
    print(op.draw)
    print(op.bookmark)
    print(op.linkplan)
    print(op.keyplan)
    print(op.opsbf_settings)
    print(op.opsbf_save)
    print(op.other)
    print(op.display_order)
    print(op.glympse)
    print(op.status_tag)
    print(op.ne)
    print(op.nw)
    print(op.se)
    print(op.sw)


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
        op.end = datetime(2030, 12, 25)
        op.save()
        op.update()
        op = T.get_operation(op.id)
        op.new_task(-32.878981, -61.022595, TaskType.DESTROY)
        print_op(op)
        
        T.get_operations(name="Cumple Ilenka")
        print_op(op)
        
