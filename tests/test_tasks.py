import unittest
from datetime import datetime

from pyenlone.v import V
from pyenlone.tasks import *
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
        self.V = V(apikey=apikey)
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
        op.update()
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
        op.new_task(" task", -32.878981, -61.022595, TaskType.DESTROY)
        tasks = op.get_tasks()
        op.get_task(tasks[0].id)
        op = T.get_operation(op.id)
        print_op(op)
        op.grant([{"type": "vteam",
                      "id": self.V.list_teams()[0].teamid,
                      "permission": "m"}])
        op.remove_grant([{"type": "vteam",
                      "id": self.V.list_teams()[0].teamid,
                      "permission": "m"}])
        msg = op.send_message({"message": "Bring booze and XMPs!"})
        op.edit_message(msg["id"], {"message": "Bring booze, XMPs and Santa hats!"})
        op.get_messages()
        op.get_users()
        op.my_grants()
        op.get_grants()

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
        task1 = op.new_task('DESTROY: Titirangi Reserve', -43.476352, 172.687535, TaskType.DESTROY,
                            portal='Titirangi Reserve',
                            portal_id="6a6993f1cb3a4e30ab24a6fcd04c4c68.16",
                            portal_init_state=portal_init_state,
                            priority=4,
                            repeat=3,
                            start=datetime(2020, 12, 25),
                            end=datetime(2030, 12, 25))
        task2 = op.new_task('DESTROY: Titirangi Reserve', -43.476352, 172.687535, TaskType.DESTROY,
                            portal='Titirangi Reserve',
                            portal_id="6a6993f1cb3a4e30ab24a6fcd04c4c68.16",
                            portal_init_state=portal_init_state,
                            priority=4,
                            repeat=3,
                            start=datetime(2020, 12, 25),
                            end=datetime(2030, 12, 25))
        task3 = op.new_task('DESTROY: Titirangi Reserve', -43.476352, 172.687535, TaskType.DESTROY,
                            portal='Titirangi Reserve',
                            portal_id="6a6993f1cb3a4e30ab24a6fcd04c4c68.16",
                            portal_init_state=portal_init_state,
                            priority=4,
                            repeat=3,
                            start=datetime(2020, 12, 25),
                            end=datetime(2030, 12, 25))
        task1.alternative = task3.id
        task2.previous = task1.id
        task1.save()
        task2.save()
        task1.update()
        task2.update()
        task1.accept()
        task1.get_acknowledge()
        task1.complete()
        task1.get_complete()
        task1.delete()
        task3.grant([{"type": "vteam",
                      "id": self.V.list_teams()[0].teamid,
                      "permission": "m"}])
        task3.remove_grant([{"type": "vteam",
                      "id": self.V.list_teams()[0].teamid,
                      "permission": "m"}])
        task3.assign([{"type": "vteam", "id": self.V.list_teams()[0].teamid}])
        op.my_grants()
        op.get_grants()



class TestTasksVOAuth(TestTasksApikey):
    def setUp(self):
        with open("TOKEN") as input_file:
            token = input_file.read()[:-1]
        self.tasks_api = Tasks(voauth=token)
        self.V = V(token=token)
        self.test_op = self.tasks_api.new_operation("Test OP", OpType.FIELD, draw=DRAW)


portal_init_state = {'artifactBrief': None,
                              'artifactDetail': None,
                              'health': 100,
                              'level': 6,
                              'mods': [{'name': 'Portal Shield',
                                        'owner': 'Xanthe02',
                                        'rarity': 'COMMON',
                                        'stats': {'MITIGATION': '30',
                                                  'REMOVAL_STICKINESS': '0'}},
                                       None,
                                       None,
                                       {'name': 'Portal Shield',
                                        'owner': 'evs99',
                                        'rarity': 'COMMON',
                                        'stats': {'MITIGATION': '30',
                                                  'REMOVAL_STICKINESS': '0'}}],
                              'ornaments': [],
                              'owner': 'evs99',
                              'resCount': 8,
                              'resonators': [{'energy': 4000,
                                              'level': 6,
                                              'owner': 'evs99'},
                                             {'energy': 4000,
                                              'level': 6,
                                              'owner': 'Xanthe02'},
                                             {'energy': 3000,
                                              'level': 5,
                                              'owner': 'Xanthe02'},
                                             {'energy': 5000,
                                              'level': 7,
                                              'owner': 'Xanthe02'},
                                             {'energy': 6000,
                                              'level': 8,
                                              'owner': 'Xanthe02'},
                                             {'energy': 5000,
                                              'level': 7,
                                              'owner': 'evs99'},
                                             {'energy': 6000,
                                              'level': 8,
                                              'owner': 'evs99'},
                                             {'energy': 4000,
                                              'level': 6,
                                              'owner': 'Xanthe02'}],
                              'team': 'R',
                              'timestamp': 1499993733589}
