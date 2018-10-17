""" Proxies do the actual API calls. """
from abc import ABC, abstractmethod

import requests
import requests_cache
from munch import munchify

from .enloneexception import EnlOneException

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
        url = self._base_url + endpoint
        params["apikey"] = self._apikey
        try:
            response = requests.get(url, params=params)
        except requests.exceptions.RequestException:
            raise EnlOneException("Error contacting enl.one servers.")
        if response and response.json()["status"] == "ok":
            return munchify(response.json()["data"])
        else:
            raise EnlOneException("enl.one API call error.")
    def post(self, endpoint, json):
        url = self._base_url + endpoint
        try:
            response = requests.post(url, params={"apikey" : self._apikey}, json=json)
        except requests.exceptions.RequestException:
            raise EnlOneException("Error contacting enl.one servers.")
        if response and response.json()["status"] == "ok":
            return munchify(response.json()["data"])
        else:
            raise EnlOneException("enl.one API call error.")

class TokenProxy(Proxy):
    def __init__(self, base_url, token, cache=0):
        self._token = token
        self._base_url = base_url + "/oauth"
        if cache > 0:
            requests_cache.install_cache('token_cache', backend='sqlite', expire_after=cache)
    def get(self, endpoint, params={}):
        url = self._base_url + endpoint
        headers = {'Authorization':'Bearer ' + self._token}
        try:
            response = requests.get(url, headers=headers, params=params)
        except requests.exceptions.RequestException:
            raise EnlOneException("Error contacting enl.one servers.")
        if response and response.json()["status"] == "ok":
            return munchify(response.json()["data"])
        else:
            raise EnlOneException("enl.one API call error.")
    def post(self, endpoint, json):
        url = self._base_url + endpoint
        headers = {'Authorization':'Bearer ' + self._token}
        try:
            response = requests.post(url, headers=headers, json=json)
        except requests.exceptions.RequestException:
            raise EnlOneException("Error contacting enl.one servers.")
        if response and response.json()["status"] == "ok":
            return munchify(response.json()["data"])
        else:
            raise EnlOneException("enl.one API call error.")

class OpenProxy:
    def get(endpoint):
        url = "https://v.enl.one/OpenApi" + endpoint
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException:
            raise EnlOneException("Error contacting enl.one servers.")
        if response and response.json()["status"] == "ok":
            return munchify(response.json()["data"])
        else:
            raise EnlOneException("enl.one API call error.")
