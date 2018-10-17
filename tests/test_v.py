import unittest
from munch import Munch

from pyenlone import V, banned

class TestV(unittest.TestCase):
    def setUp(self):
        with open("APIKEY") as input_file:
            apikey = input_file.read()[:-1]
        self.key_api = V(apikey=apikey)
    def test_search(self):
        result = self.key_api.search_one(query="QuanticPotato")
        assert "enlid" in result
        result = self.key_api.search_one(telegram="QuanticPotato")
        assert "enlid" in result
        result = self.key_api.search_one(lat=-33.154519, lon=-60.519308)
        assert "enlid" in result
    def test_is_ok(self):
        assert self.key_api.is_ok(self.key_api.search_one(query="QuanticPotato"))
    def test_distance(self):
        enlid1 = self.key_api.search_one(query="QuanticPotato")["enlid"]
        enlid2 = self.key_api.search_one(query="abstractpainter")["enlid"]
        result = self.key_api.distance(enlid1, enlid2)
        assert len(result) == 2
    def test_trust(self):
        enlid1 = self.key_api.search_one(query="QuanticPotato")["enlid"]
        result = self.key_api.trust(enlid1)
        assert result["agent"] == "QuanticPotato"
    def test_bulk_info(self):
        agent = self.key_api.whoami()
        result = self.key_api.bulk_info([agent.telegramid], array=True, telegramid=True)
        assert type(result) is list
        result = self.key_api.bulk_info([agent.enlid])
        assert type(result) is Munch
        result = self.key_api.bulk_info([agent.gid], gid=True)
        assert type(result) is Munch
    def test_list_teams(self):
        result = self.key_api.list_teams()
        assert type(result) is list
    # You need at least one team to test this
    def test_team_details(self):
        result = self.key_api.team_details(self.key_api.list_teams()[0].teamid)
        assert type(result) is list
    def test_location(self):
        enlid = self.key_api.search_one(query="QuanticPotato").enlid
        result = self.key_api.location(enlid)
    def test_whoami(self):
        result = self.key_api.whoami()
        assert "agent" in result
    @unittest.skip
    def test_banned(self):
        gid = self.key_api.search_one(query="PATHF1ND3R", inactive=True).gid
        assert banned(gid)
    @unittest.skip
    def test_token(self):
        with open("TOKEN") as input_file:
            token = input_file.read()[:-1]
        self.token_api = V(token=token)

        result = self.token_api.search(query="QuanticPotato")
        assert "enlid" in result[0]

        result = self.token_api.distance(enlid1, enlid2)
        assert result == ["QuanticPotato", "abstractpainter"]

        result = self.token_api.trust(enlid1)
        assert result["agent"] == "QuanticPotato"

        result = self.token_api.bulk_info([agent.enlid])
        assert type(result) is Munch
        result = self.token_api.bulk_info([agent.gid], gid=True)
        assert type(result) is Munch

        result = self.token_api.list_teams()
        assert type(result) is list

        result = self.token_api.team_details(self.key_api.list_teams()[0].teamid)
        assert type(result) is list
        assert "role" in result[0]

        assert "lat" in result
        result = self.token_api.location(enlid=enlid)
        assert "lat" in result
