from proxy import Proxy, TokenProxy, KeyProxy
from enloneexception import EnlOneException

class V:
    _proxy : Proxy
    _base_url = "v.enl.one/"
    def __init__(self, **kwargs):
        if "token" in kwargs:
            _proxy = TokenProxy(_base_url, kwargs["token"])
        elif "apikey" in kwargs:
            _proxy = KeyProxy(_base_url, kwargs["apikey"])
        else:
            raise EnlOneException("You need to either provide token or apikey as keyword argument.")
    def search(self):
        raise EnlOneException("Not implemented yet.")
    def distance(self):
        raise EnlOneException("Not implemented yet.")
    def bulk_search(self):
        raise EnlOneException("Not implemented yet.")
    def location(self):
        raise EnlOneException("Not implemented yet.")
    def whoami(self):
        raise EnlOneException("Not implemented yet.")
    def banned(self):
        raise EnlOneException("Not implemented yet.")
    # Estos los tomo de la v2
    def list_teams(self):
        raise EnlOneException("Not implemented yet.")
    def team_details(self):
        raise EnlOneException("Not implemented yet.")
