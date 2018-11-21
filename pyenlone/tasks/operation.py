from enum import Enum
from datetime import datetime
from typing import Optional, List, Tuple, Dict, NewType

from ..v import IGN
from .task import Task, TaskType, TaskID
from .message import MessageID

OpID = NewType("OpID", int)
Draw = NewType("Draw", str)
Arcs = NewType("Arcs", str)
Bookmark = NewType("Bookmark", str)
Linkplan = NewType("Linkplan", str)
Keyplan = NewType("Keyplan", str)
LatLng = NewType("LatLng", str)

def _fix_task_params(params):
    params["todo"] = todo.value
    if "portal_id" in params:
        params["portalID"] = params["portal_id"]
    if "link_target" in params:
        params["linkTarget"] = params["link_target"]
    if "group_name" in params:
        params["groupName"] = params["group_name"]
    if "portal_image" in params:
        params["portalImage"] = params["portal_image"]

class OpType(Enum):
    FIELD = "field"
    FIELD_DEFENSE = "field-defense"
    AREA = "area"
    LINKSTAR = "linkstar"
    LINKART = "linkart"
    OTHER = "other"

class Operation:
    """
    A Tasks API operation. Don't create operations manually, get them with
        Tasks.new_operation
        Tasks.get_operations
        Tasks.search_operations
    """
    def __init__(self, proxy, api_result):
        self._proxy = proxy

        self._id = OpID(api_result["id"])
        self._from_api(api_result)

    def _from_api(self, api_result):
        self._name = IGN(api_result["name"])
        self._owner = api_result["owner"]
        self._start = datetime.fromtimestamp(api_result["start"] / 1000)
        if "end" in api_result:
            self._end = datetime.fromtimestamp(api_result["end"] / 1000)
        else:
            self._end = None
        self._type = OpType(api_result["type"])
        if "agentDraw" in api_result:
            self._agent_draw = Draw(api_result["agentDraw"])
        else:
            self._agent_draw = None
        if "draw" in api_result:
            self._draw = Draw(api_result["draw"])
        else:
            self._draw = None
        if "bookmark" in api_result:
            self._bookmark = Bookmark(api_result["bookmark"])
        else:
            self._bookmark = None
        if "linkplan" in api_result:
            self._linkplan = api_result["linkplan"]
        else:
            self._linkplan = None
        if "keyplan" in api_result:
            self._keyplan = api_result["linkplan"]
        else:
            self._keyplan = None
        if "opsbf_settings" in api_result:
            self._opsbf_settings = api_result["opsbf_settings"]
        else:
            self._opsbf_settings = None
        if "opsbf_save" in api_result:
            self._opsbf_save = api_result["opsbf_save"]
        else:
            self._opsbf_save = None
        if "other" in api_result:
            self._other = api_result["other"]
        else:
            self._other = None
        if "displayOrder" in api_result:
            self._display_order = api_result["displayOrder"]
        else:
            self._display_order = None
        if "glympse" in api_result:
            self._glympse = api_result["glympse"]
        else:
            self._glympse = None
        if "statusTag" in api_result:
            self.status_tag = api_result["statusTag"]
        else:
            self._status_tag = None
        if "ne" in api_result:
            self._ne = LatLng(api_result["ne"])
        else:
            self._ne = None
        if "nw" in api_result:
            self._nw = LatLng(api_result["nw"])
        else:
            self._nw = None
        if "se" in api_result:
            self._se = LatLng(api_result["se"])
        else:
            self._se = None
        if "sw" in api_result:
            self._sw = LatLng(api_result["sw"])
        else:
            self._sw = None

    def _to_api(self):
        return {
            "name": self._name,
            "start": self._start.timestamp() * 1000,
            "end": self._end.timestamp() * 1000 if self._end else None,
            "type": self._type.value,
            "agentDraw": self._agent_draw,
            "draw": self._draw,
            "bookmark": self._bookmark,
            "linkplan": self._linkplan,
            "keyplan": self._keyplan,
            "opsbf_settings": self._opsbf_settings,
            "opsbf_save": self._opsbf_save,
            "other": self._other,
            "displayOrder": self._display_order,
            "glympse": self._glympse,
            "statusTag": self._status_tag,
            "ne": self._ne,
            "nw": self._nw,
            "se": self._se,
            "sw": self._sw
        }

    @property
    def id(self) -> int:
        """
        ID of the Operation.
        """
        return self._id

    @property
    def name(self) -> Optional[str]:
        """
        Name of the Operation.
        """
        return self._name

    @property
    def owner(self) -> IGN:
        """
        Owner of the operation.
        """
        return self._owner

    @property
    def start(self) -> datetime:
        """
        When the operations starts.
        """
        return self._start

    @property
    def end(self) -> Optional[datetime]:
        """
        When the operations ends.
        """
        return self._end

    @property
    def type(self) -> OpType:
        """
        What kind of operation.
        """
        return self._type

    @property
    def agent_draw(self) -> Draw:
        """
        A draw for that operation that is visible to all agents
        with read access.
        """
        return self._agent_draw

    @property
    def draw(self) -> Draw:
        """
         The draw for that operation. Only visible to Owner and Operator!
        """
        return self._draw

    @property
    def arcs(self) -> Arcs:
        pass

    @property
    def bookmark(self) -> Bookmark:
        """
         The bookmarks for that operation. Only visible to Owner and Operator!
        """
        return self._bookmark

    @property
    def linkplan(self) -> Linkplan:
        """
         The draw for that operation. Only visible to Owner and Operator!
        """
        return self._linkplan

    @property
    def keyplan(self) -> Keyplan:
        """
         The keyplan for that operation. Only visible to Owner and Operator!
        """
        return self._keyplan

    @property
    def opsbf_settings(self) -> str:
        """
         OPSBF Settings for that operation. Only visible to Owner and Operator!
        """
        return self._opsbf_settings

    @property
    def opsbf_save(self) -> str:
        """
         OPSBF Save for that operation. Only visible to Owner and Operator!
        """
        return self._opsbf_save

    @property
    def other(self) -> Dict:
        """
         More data regarding that operation. An Object (Hash dictionary) with
         name:value pairs. You can store whatever you want. Only visible to
         Owner and Operator!
        """
        return self._other

    @property
    def display_order(self) -> List:
        """
         Array of task IDs as integers to indicate the order the tasks should
         be displayed in clients.
        """
        return self._display_order

    @property
    def glympse(self) -> str:
        """
         The glympse tag for that operation, can be presented on client as a
         link to app: http://glympse.com/!your_group_name
         (always starts with !).
        """
        return self._glympse

    @property
    def status_tag(self) -> str:
        """
         The tag for that operation, to share location in this operation.
        """
        return self._status_tag

    @property
    def ne(self) -> LatLng:
        """
         Area Management - the Box defining the area.
        """
        return self._ne

    @property
    def nw(self) -> LatLng:
        """
         Area Management - the Box defining the area.
        """
        return self._nw

    @property
    def se(self) -> LatLng:
        """
         Area Management - the Box defining the area.
        """
        return self._se

    @property
    def sw(self) -> LatLng:
        """
         Area Management - the Box defining the area.
        """
        return self._sw

    @name.setter
    def name(self, value: str):
        self._name = value

    @start.setter
    def start(self, value: datetime):
        self._start = value

    @end.setter
    def end(self, value: datetime):
        self._end = value

    @type.setter
    def type(self, value: OpType):
        self._type = value

    @agent_draw.setter
    def agent_draw(self, value: Draw):
        self._agent_draw = value

    @draw.setter
    def draw(self, value: Draw):
        self._draw = value

    @bookmark.setter
    def bookmark(self, value: Bookmark):
        self._bookmark = value

    @linkplan.setter
    def linkplan(self, value: Linkplan):
        self._linkplan = value

    @keyplan.setter
    def keyplan(self, value: Keyplan):
        self._keyplan = value

    @opsbf_settings.setter
    def opsbf_settings(self, value):
        self._opsbf_settings = value

    @opsbf_save.setter
    def opsbf_save(self, value):
        self._opsbf_save = value

    @other.setter
    def other(self, value: Dict):
        self._other = value

    @display_order.setter
    def display_order(self, value: List[TaskID]):
        self._display_order = value

    @glympse.setter
    def glympse(self, value: str):
        self._glympse = value

    @status_tag.setter
    def status_tag(self, value: str):
        self._status_tag = value

    @ne.setter
    def ne(self, value: LatLng):
        self._ne = value

    @nw.setter
    def nw(self, value: LatLng):
        self._nw = value

    @ne.setter
    def ne(self, value: LatLng):
        self._ne = value

    @nw.setter
    def nw(self, value: LatLng):
        self._nw = value

    def _base_url(self):
        return "/op/" + str(self.id)

    def save(self):
        """
        Save all changes to Tasks server.
        """
        self._proxy.put(self._base_url(), self._to_api())

    def update(self):
        """
        Update data from Tasks servers.
        """
        self._from_api(self._proxy.get(self._base_url()))

    def delete(self):
        """
        Delete this operation.
        Also deletes all tasks, messages and grants.
        """
        self._proxy.delete(self._base_url())

    def new_task(self, name: str, lat: float, lon: float, todo: TaskType, **params) -> Task:
        """
        Add a new task.
        Requires parameters are location and type.
        Aditional initializing parameters can be set in keyword arguments.
        """
        params["name"] = name
        params["lat"] = lat
        params["lon"] = lon
        _fix_task_params(params)
        api_res = self._proxy.post(self._base_url() + "/task", params)
        return Task(self._proxy, api_res)

    def bulk_new_task(self, tasks: List[Dict]) -> List[Task]:
        """
        Bulk add new tasks.
        Parameter is a list of dictionaries with the parameters of each task.
        Each one must have al least lat, lon, type and name.
        """
        for task in tasks:
            if "portal_id" in task:
                task["portalID"] = task["portal_id"]
            if "link_target" in task:
                task["linkTarget"] = task["link_target"]
            if "group_name" in task:
                task["groupName"] = task["group_name"]
            if "portal_image" in task:
                task["portalImage"] = task["portal_image"]
            task["todo"] = task["todo"].value
        return [Task(self._proxy, api_res) for api_res
                in self._proxy.post(self._base_url() + "/task", tasks)]

    def get_task(self, id):
        """
        Retrieve specific task.
        """
        return Task(self._proxy, self._proxy.get(self._base_url() + "/task/" + str(id))[0])

    def get_tasks(self, **filters) -> List[Task]:
        """
        Retrieve all task of this operation the user can see.
        Aditional search filters can be queried using the keyword arguments.
        """
        _fix_task_params(filters)
        return [Task(self._proxy, api_res) for api_res
                in self._proxy.get(self._base_url() + "/task")]

    def add_grant(self):
        """
        Grant permission.
        """
        pass

    def remove_grant(self):
        """
        Remove grant.
        """
        pass

    def get_grants(self):
        """
        Retrieve all grants on this op.
        """
        pass

    def my_grants(self):
        """
        Retrieve all grants applicable to this user.
        """
        pass

    def send_message(self, text: str) -> MessageID:
        """
        Post new message to the op-chat.
        """
        pass

    def get_message(self, message_id):
        """
        Retrieve a specific message.
        """
        pass


    def get_messages(self, offset=0):
        """
        Retrieve up to 50 messages, add offset to query more
        """
        pass

    def get_users(self):
        """
        Returns Array of agents with permissions.
        """
        pass

    def sync_rocks_comm(self):
        """
        For Webhooks from rocks
        """
        pass
