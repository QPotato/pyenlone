"""
Implements Tasks API methods.
More info on: https://wiki.enl.one/doku.php?id=t_basic_documentation
"""
from abc import ABC, abstractmethod
from typing import Tuple

from .operation import Operation, OpID
from .task import Task
from .message import Message
from .grant import Grant
from .._proxy import TokenProxy, KeyProxy


__all__ = [Operation, Task, Message, Grant]


class Tasks:
    def __init__(self, apikey: Optional[str] = None, voauth: Optional[str] = None, rocks=None: str, enlio=None:str, cache=0: int):
        self._proxy = TokenProxy("https://tasks.enl.one", token, cache=cache)
        pass

    def new_operation(name: str, optype: OpType, box: OpBox) -> Operation:
        pass

    def get_operations(**kwargs) -> List[Operation]:
        pass

    def search_operations(lat: float, lon: float, km: float) -> List[Operation]:
        pass

    def get_tasks(**kwargs) -> List[Task]:
        pass

    def search_tasks(lat: float, lon: float, km: float) -> List[Task]:
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
