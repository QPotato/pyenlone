from ._proxy import TokenProxy, KeyProxy, OpenProxy
from ._oauth import VOAuth
from .enloneexception import EnlOneException

def banned(gid):
    return OpenProxy.get("/banned/" + gid)

class V:
    _base_url = "https://v.enl.one"
    def __init__(self, cache=0, **kwargs):
        if "token" in kwargs:
            self._proxy = TokenProxy(self._base_url, kwargs["token"], cache=cache)
            self._oauth = VOAuth(self._proxy)
        elif "apikey" in kwargs:
            self._proxy = KeyProxy(self._base_url, kwargs["apikey"], cache=cache)
        else:
            raise EnlOneException("You need to either provide token or apikey as keyword argument.")

    # v1 general endpoints
    def trust(self, enlid):
        return self._proxy.get("/api/v1/agent/" + enlid + "/trust")
    def search(self, **kwargs):
        return self._proxy.get("/api/v1/search", params=kwargs)
    def distance(self, enlid1, enlid2):
        return self._proxy.get("/api/v1/agent/" + enlid1 + "/" + enlid2).hops
    def bulk_info(self, ids, telegramid=False, gid=False, array=False):
        url = "/api/v1/bulk/agent/info"
        if telegramid:
            url += "/telegramid"
        if gid:
            url += "/gid"
        if array:
            url += "/array"
        return self._proxy.post(url, ids)
    def location(self, enlid):
        return self._proxy.get("/api/v1/agent/" + enlid + "/location")
    def whoami(self):
        return self._proxy.get("/api/v1/whoami")
    #TODO: profile pictures

    # v2 endpoints
    def list_teams(self):
        return self._proxy.get("/api/v2/teams", )
    def team_details(self, teamid):
        return self._proxy.get("/api/v2/teams/" + str(teamid))

    # OAuth specifics
    def profile(self):
        return self._oauth.profile()
    def googledata(self):
        return self._oauth.googledata()
    def email(self):
        return self._oauth.email()
    def telegram(self):
        return self._oauth.telegram()

    # Short-handers
    def search_one(self, **kwargs):
        return self.search(**kwargs)[0]
    def is_ok(self, agent):
        return agent.verified \
               and agent.active \
               and not agent.quarantine \
               and not agent.blacklisted \
               and not agent.banned_by_nia
