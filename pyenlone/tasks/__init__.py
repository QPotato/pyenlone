"""
Implements Tasks API methods.
More info on: https://wiki.enl.one/doku.php?id=t_basic_documentation
"""
from typing import Tuple, List, Optional

from .operation import Operation, OpID, OpType
from .task import Task
from .message import Message
from .grant import Grant
from .._proxy import TokenProxy, KeyProxy


__all__ = [Operation, Task, Message, Grant]


class Tasks:
    def __init__(self,
                 apikey: Optional[str] = None,
                 voauth: Optional[str] = None,
                 rocks: Optional[str] = None,
                 enlio: Optional[str] = None,
                 cache: int = 0):
        self._proxy = TokenProxy("https://tasks.enl.one", token, cache=cache)
        pass

    def get_operation(id: OpID):
        """
         Retrive Operation.
        """
        pass

    def get_operations(self, **filters) -> List[Operation]:
        """
         Get all operations user is owner, operator or can see.
        """
        pass

    def new_operation(self, name: str, op_type: OpType, **params) -> Operation:
        """
         Add new operation.
        """
        params["name"] = name
        params["optype"] = op_type.value
        api_res = self._proxy.post("/op", params)
        return Operation(self._proxy, api_res)

    def search_operations(lat: float, lon: float, km: int) -> List[Operation]:
        """
        Returns Array of ops with tasks in range
        (lat = float; lon = float; range = radius in KM)
        """
        pass

    def get_tasks(self, **filters) -> List[Task]:
        """
        Retrieve all tasks visible to the user,
        from all operations.
        """
        pass

    def search_tasks(lat: float, lon: float, km: float) -> List[Task]:
        """
        Find all tasks in a radius of km from lat/lon visible to the user,
        from all operations.
        """
        pass


class TasksAPIFactory():
    def __init__(self, token, cache=0):
        self._proxy = TokenProxy("https://tasks.enl.one", token, cache=cache)
        pass

    def new_operation(self, name: str, type: OpType,
                      box: Box=None) -> Operation:
        return Operation(_proxy)

    def load_operation(self, id: int) -> Operation:
        pass
