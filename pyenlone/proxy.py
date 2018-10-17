""" Proxies do the actual API calls. """
from abc import ABC, abstractmethod
import requests
import requests_cache
from munch import Munch
from enloneexception import EnlOneException

class Proxy(ABC):
    @abstractmethod
    def get(self, endpoint, params): pass

class KeyProxy(Proxy):
    def __init__(self, base_url, apikey, cache=0):
        self._apikey = apikey
        self._base_url = base_url
        if cache > 0:
            requests_cache.install_cache('apikey_cache', backend='sqlite', expire_after=cache)
    def get(self, endpoint, params={}):
        url = self._base_url + "/api" + endpoint
        data = dict({"apikey" : self._apikey}, **params)
        try:
            response = requests.get(url, params=data)
        except requests.exceptions.RequestException:
            raise EnlOneException("Error contacting enl.one servers.")
        if response:
            return Munch(response.json()["data"])
        else:
            raise EnlOneException("enl.one API call error.")


class TokenProxy(Proxy):
    def __init__(self, base_url, token):
        self._token = token
        self._base_url = base_url
        if cache > 0:
            requests_cache.install_cache('token_cache', backend='sqlite', expire_after=cache)
        if "user_id" not in self._get("/verify"):
            raise EnlOneException("enl.one API call error.")
    def _get(self, endpoint, params):
        url = self._base_url + "/oauth" + endpoint
        headers = {'Authorization':'Bearer ' + self._token}
        try:
            response = requests.get(url, headers=headers, params=params)
        except requests.exceptions.RequestException:
            raise EnlOneException("Error contacting enl.one servers.")
        if response:
            return Munch(response.json()["data"])
        else:
            raise EnlOneException("enl.one API call error.")
    def get(self, endpoint, params):
        return self._get("/api", params)
