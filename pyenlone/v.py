from ._proxy import TokenProxy, KeyProxy, open_request
from .enloneexception import EnlOneException

def banned(gid):
    return open_request("/banned/" + gid)

class V:
    _base_url = "https://v.enl.one"
    def __init__(self, cache=0, **kwargs):
        if "token" in kwargs:
            self._proxy = TokenProxy(self._base_url, kwargs["token"], cache=cache)
        elif "apikey" in kwargs:
            self._proxy = KeyProxy(self._base_url, kwargs["apikey"], cache=cache)
        else:
            raise EnlOneException("You need to either provide token or apikey as keyword argument.")

    # v1 endpoints
    def trust(self, enlid):
        return self._proxy.get("/v1/agent/" + enlid + "/trust")
    def search(self, **kwargs):
        return self._proxy.get("/v1/search", params=kwargs)
    def distance(self, enlid1, enlid2):
        return self._proxy.get("/v1/agent/" + enlid1 + "/" + enlid2).hops
    def bulk_info(self, ids, telegramid=False, gid=False, array=False):
        url = "/v1/bulk/agent/info"
        if telegramid:
            url += "/telegramid"
        if gid:
            url += "/gid"
        if array:
            url += "/array"
        return self._proxy.post(url, ids)
    def location(self, enlid):
        return self._proxy.get("/v1/agent/" + enlid + "/location")
    def whoami(self):
        return self._proxy.get("/v1/whoami")
    #TODO: profile pictures

    # v2 endpoints
    def list_teams(self):
        return self._proxy.get("/v2/teams", )
    def team_details(self, teamid):
        return self._proxy.get("/v2/teams/" + str(teamid))

    # Short-handers
    def search_one(self, **kwargs):
        return self.search(**kwargs)[0]
    def is_ok(self, agent):
        return agent.verified \
               and agent.active \
               and not agent.quarantine \
               and not agent.blacklisted \
               and not agent.banned_by_nia
