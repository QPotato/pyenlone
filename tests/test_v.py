import unittest
from .pyenlone import V

class TestV(unittest.TestCase):
    def setUp():
        self.apikey = input("apikey: ")
        self.token = input("oauth token: ")
        key_api = V(apikey=self.apikey)
        token_api = V(token=self.token
    def test_search():
        result = key_api.search_one(query="QuanticPotato")
        self.assertTrue("enlid" in result)
        result = key_api.search_one(telegram="QuanticPotato")
        self.assertTrue("enlid" in result)
        result = key_api.search_one(lat="-33.154519", lon="-60.519308")
        self.assertTrue("enlid" in result)
        result = token_api.search(query="QuanticPotato")
        self.assertTrue("enlid" in result[0])
    def test_distance():
        enlid1 = key_api.search_one(query="QuanticPotato")["enlid"]
        enlid2 = key_api.search_one(query="abstractpainter")["enlid"]
        result = key_api.distance(enlid1, enlid2)
        self.assertEqual(result, ["QuanticPotato", "abstractpainter"])
        result = token_api.distance(enlid1, enlid2)
        self.assertEqual(result, ["QuanticPotato", "abstractpainter"])
    def test_info():
        enlid1 = key_api.search_one(query="QuanticPotato")["enlid"]
        result = key_api.info(enlid1)
        self.assertTrue(result["agent"], "QuanticPotato")
        result = token_api.info(enlid1)
        self.assertTrue(result["agent"], "QuanticPotato")
    def test_bulk_info():
        result = key_api.bulk_info(["QuanticPotato", "abstractpainter", "Potusito"], array=True, telegram=True)
        result = key_api.info(enlid1)
        self.assertTrue(result["agent"], "QuanticPotato")
