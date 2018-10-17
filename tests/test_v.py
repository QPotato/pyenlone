import unittest
from .pyenlone import V, banned

class TestV(unittest.TestCase):
    def setUp(self):
        self.apikey = input("apikey: ")
        self.token = input("oauth token: ")
        key_api = V(apikey=self.apikey)
        token_api = V(token=self.token)
    def test_search(self):
        result = key_api.search_one(query="QuanticPotato")
        assert "enlid" in result
        result = key_api.search_one(telegram="QuanticPotato")
        assert "enlid" in result
        result = key_api.search_one(lat=-33.154519, lon=-60.519308)
        assert "enlid" in result
        result = key_api.search_one(lat=51.43209462844014, lon=11.865234375, range=100, blacklisted=True)
        assert "enlid" in result
        result = token_api.search(query="QuanticPotato")
        assert "enlid" in result[0]
    def test_trusty(self):
        assert key_api.trusty(telegram="QuanticPotato")
    def test_distance(self):
        enlid1 = key_api.search_one(query="QuanticPotato")["enlid"]
        enlid2 = key_api.search_one(query="abstractpainter")["enlid"]
        result = key_api.distance(enlid1, enlid2)
        assert result == ["QuanticPotato", "abstractpainter"]
        result = token_api.distance(enlid1, enlid2)
        assert result == ["QuanticPotato", "abstractpainter"]
    def test_info(self):
        enlid1 = key_api.search_one(query="QuanticPotato")["enlid"]
        result = key_api.info(enlid1)
        assert result["agent"] == "QuanticPotato"
        result = token_api.info(enlid1)
        assert result["agent"] == "QuanticPotato"
    def test_bulk_info(self):
        result = key_api.bulk_info(["QuanticPotato", "abstractpainter", "Potusito"], array=True, telegramid=True)
        assert result[0].agent = "QuanticPotato"
        result = token_api.bulk_info(["QuanticPotato", "abstractpainter", "Potusito"], array=True, telegramid=True)
        assert result[0].agent = "QuanticPotato"
    def test_list_teams(self):
        result = key_api.list_teams()
        assert type(result) is list
        result = token_api.list_teams()
        assert type(result) is list
    # You need at least one team to test this
    def test_team_details(self):
        result = key_api.team_details(key_api.list_teams()[0].teamid)
        assert type(result) is list
        assert "role" in result[0]
        result = token_api.team_details(key_api.list_teams()[0].teamid)
        assert type(result) is list
        assert "role" in result[0]
    def test_location(self):
        enlid = key_api.search_one(query="QuanticPotato").enlid
        result = key_api.location(enlid=enlid)
        assert "lat" in result
        result = token_api.location(enlid=enlid)
        assert "lat" in result
    def test_whoami(self):
        result = key_api.whoami()
        assert "agent" in result
    def test_banned(self):
        assert banned("PATHF1ND3R")
