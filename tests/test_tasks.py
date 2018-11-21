import unittest
from datetime import datetime

from pyenlone.tasks import Tasks, OpType, TaskType
from pyenlone.enloneexception import NotImplementedByBackendException

DRAW = """[{"type":"polyline","latLngs":[{"lat":-32.777775,"lng":-61.604255},{"lat":-33.258328,"lng":-58.023684}],"color":"#a24ac3"}]"""

DRAW2 = """[{"type":"polyline","latLngs":[{"lat":-32.191319,"lng":-64.255717},{"lat":-32.997068,"lng":-60.768294}],"color":"#a24ac3"},{"type":"polyline","latLngs":[{"lat":-34.157474,"lng":-58.977627},{"lat":-34.04441,"lng":-53.534274}],"color":"#a24ac3"},{"type":"polyline","latLngs":[{"lat":-37.253639,"lng":-56.97083},{"lat":-33.762181,"lng":-60.646054}],"color":"#a24ac3"},{"type":"polyline","latLngs":[{"lat":-32.999731,"lng":-60.77304},{"lat":-35.977956,"lng":-62.728776}],"color":"#a24ac3"},{"type":"polyline","latLngs":[{"lat":-38.580598,"lng":-58.723627},{"lat":-34.157474,"lng":-58.977627}],"color":"#a24ac3"}]"""

BKMK = """{"maps":{"idOthers":{"label":"Others","state":1,"bkmrk":{}}},"portals":{"idOthers":{"label":"Others","state":1,"uri":0,"visibility":"V","bkmrk":{"id1542752992823087":{"guid":"7c00cbc82c09483a82bbc594234cf3cb.16","latlng":"-32.999731,-60.77304","label":"El Ferroviario"},"id1542752995144116":{"guid":"ddcc4d05ee304dc2900fb7279ef841b1.16","latlng":"-32.878981,-61.022595","label":"Busto De San Martín"},"id1542752998759275":{"guid":"d50b2f9716f543868191be3601e00391.16","latlng":"-33.154519,-60.519308","label":"Santo "},"id1542753049566346":{"guid":"422e4d4e9b9f4e5281f0d17ca5867ba3.16","latlng":"-32.759057,-64.333224","label":"HOMENAJE A LOS COMBATIENTES DE MALVINAS"}}}}}"""


def print_op(op):
    print(op.id)
    print(op.name)
    print(op.owner)
    print(op.start)
    print(op.end)
    print(op.type)
    print(op.agent_draw)
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


class TestTasksApikey(unittest.TestCase):
    def setUp(self):
        with open("APIKEY") as input_file:
            apikey = input_file.read()[:-1]
        self.tasks_api = Tasks(apikey=apikey)
        self.test_op = self.tasks_api.new_operation("Test OP", OpType.FIELD, draw=DRAW)

    def tearDown(self):
        self.test_op.delete()

    def test_op(self):
        T = self.tasks_api
        op = self.test_op
        print_op(op)
        T.get_operations()
        T.search_operations(-32.878981, -61.022595, 350)
        T.get_tasks()
        self.assertRaises(NotImplementedByBackendException, T.search_tasks, -32.878981, -61.022595, 350)
        op.end = datetime(2030, 12, 25)
        op.name = "Test2"
        op.start = datetime(2018, 11, 10, 10, 0, 0)
        op.end = datetime(2028, 11, 10, 10, 0, 0)
        op.type = OpType.AREA
        op.agent_draw = DRAW
        op.draw = DRAW2
        op.bookmark = BKMK
        op.linkplan = "asd"
        op.keyplan = "asd"
        op.opsbf_settings = "asd"
        op.opsbf_save = "asd"
        op.other = {"other": "test"}
        op.glympe = "asd"
        op.status_tag = "asd"
        op.save()
        op.update()
        op.new_task("Test task", -32.878981, -61.022595, TaskType.DESTROY)
        op.bulk_new_task([{
            "name": "Test task",
            "lat": -32.878981,
            "lon": -61.022595,
            "todo":TaskType.DESTROY
        }, {
            "name": "Test task",
            "lat": -32.878981,
            "lon": -61.022595,
            "todo":TaskType.DESTROY
        }])
        tasks = op.get_tasks()
        op.get_task(tasks[0].id)
        op = T.get_operation(op.id)
        print_op(op)
        """
        [{'createdAt': 1542744594375,
          'displayOrder': [403094, 403095, 403096, 403097],
          'id': 2300,
          'name': 'Estrategia Buenos Aires',
          'ne': '-34.255178,-58.37169',
          'nw': '-34.665379,-59.84107',
          'other': {},
          'owner': 'QuanticPotato',
          'se': '-35.526508,-58.37169',
          'start': 1542744594375,
          'statusTag': '4762bae678deefdf45546fb2250213447eaf4296',
          'sw': '-35.943336,-59.84107',
          'type': 'area',
          'updatedAt': 1542745040104}]
        """

    def test_task(self):
        T = self.tasks_api
        op = self.test_op
        op.new_task("Test task", -32.878981, -61.022595, TaskType.DESTROY)


@unittest.skip
class TestTasksVOAuth(TestTasksApikey):
    def setUp(self):
        with open("TOKEN") as input_file:
            apikey = input_file.read()[:-1]
        self.tasks_api = Tasks(VOAuth=apikey)
        self.test_op = self.tasks_api.new_operation("Test OP", OpType.FIELD, draw=DRAW)
