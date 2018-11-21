"""
Implements Tasks API methods.
More info on: https://wiki.enl.one/doku.php?id=t_basic_documentation
"""
from typing import List, Optional

from .operation import Operation, OpID, OpType, _fix_task_params
from .task import Task, TaskID, TaskType, PortalID
from .message import Message, MessageID
from .grant import Grant
from .._proxy import TokenProxy, KeyProxy
from ..enloneexception import NotImplementedByBackendException

__all__ = ["Operation", "OpID", "OpType",
           "Task", "TaskID",  "TaskType", "PortalID",
           "Message", "MessageID", "Grant", "Tasks"]


def _fix_op_params(params):
    if "type" in params:
        params["type"] = params["type"].value
    if "agent_draw" in params:
        params["agentDraw"] = params["agent_draw"]
    if "display_order" in params:
        params["displayOrder"] = params["agent_draw"]
    if "status_tag" in params:
        params["statusTag"] = params["status_tag"]

class Tasks:
    def __init__(self,
                 apikey: Optional[str] = None,
                 voauth: Optional[str] = None,
                 rocks: Optional[str] = None,
                 enlio: Optional[str] = None,
                 google: Optional[str] = None,
                 firebase: Optional[str] = None,
                 cache: int = 0):
        url = "https://tasks.enl.one"
        if apikey:
            self._proxy = KeyProxy(url + "/api", apikey, cache=cache)
        elif voauth:
            self._proxy = TokenProxy(url + "/oauth", "VOAuth " + token, cache=cache)
        elif rocks:
            self._proxy = TokenProxy(url + "/rocks", "Rocks " + token, cache=cache)
        elif enlio:
            self._proxy = TokenProxy(url + "/enlio", "EnlIO " + token, cache=cache)
        elif google:
            self._proxy = TokenProxy(url + "/gapi", "Google " + token, cache=cache)
        elif firebase:
            self._proxy = TokenProxy(url + "/firebase", "FirebaseJWT " + token, cache=cache)
            
    def get_operation(self, id: OpID):
        """
         Retrive Operation.
        """
        return Operation(self._proxy, self._proxy.get("/op/" + str(id)))

    def get_operations(self, **filters) -> List[Operation]:
        """
         Get all operations user is owner, operator or can see.
        """
        _fix_op_params(filters)
        return [Operation(self._proxy, api_res) for api_res
                in self._proxy.get("/ops", filters)]

    def new_operation(self, name: str, op_type: OpType, **params) -> Operation:
        """
         Add new operation.
         Required parameters are name and type.
         Aditional initializing arguments can be passes in keyword arguments.
        """
        params["name"] = name
        params["type"] = op_type
        _fix_op_params(params)
        return Operation(self._proxy, self._proxy.post("/op", params))

    def search_operations(self, lat: float, lon: float, km: int, **filters) -> List[Operation]:
        """
        Find all operations with tasks in a radius of km from lat/lon visible
        to the user.
        Aditional search filters can be passed in keyword arguments.
        """
        _fix_op_params(filters)
        return [Operation(self._proxy, api_res) for api_res
                in self._proxy.get("/ops/search"
                                   + "/" + str(lat)
                                   + "/" + str(lon)
                                   + "/" + str(km),
                                   filters)]

    def get_tasks(self, **filters) -> List[Task]:
        """
        Retrieve all tasks visible to the user,
        from all operations.
        """
        _fix_task_params(filters)
        return [Task(self._proxy, api_res) for api_res
                in self._proxy.get("/tasks", filters)]


    def search_tasks(self, lat: float, lon: float, km: float, **filters) -> List[Task]:
        """
        Find all tasks in a radius of km from lat/lon visible to the user,
        from all operations.
        Aditional search filters can be passed in keyword arguments.
        """
        _fix_task_params(filters)
        raise NotImplementedByBackendException
        return [Task(self._proxy, api_res) for api_res
                in self._proxy.get("/tasks/search"
                                   + "/" + str(lat)
                                   + "/" + str(lon)
                                   + "/" + str(km),
                                   filters)]
