from enum import Enum
from datetime import Datetime
from typing import Optional, List, Tuple, Dict, NewType

from .v import IGN
from task import Task, TaskType
OpID = NewType("OpID", int)
Draw = NewType("Draw", str)
Bookmark = NewType("Bookmark", str)
LatLng = NewType("LatLng", str)


class OpType(Enum):
    FIELD = "field"
    FIELD_DEFENSE = "field-defense"
    AREA = "area"
    LINKSTAR = "linkstar"
    LINKART = "linkart"
    OTHER = "other"


class Operation:
    def __init__(self, proxy, api_result):
        self._proxy = proxy

        self._id = OpID(api_result["id"])
        self._from_api(api_result)

    def _from_api(self, api_result):
        self._name = IGN(api_result["name"])
        self._owner = api_result["owner"]
        self._start = Datetime(api_result["start"])
        if "end" in api_result:
            self._end = Datetime(api_result["end"])
        else:
            self._end = None
        self._type = OpType(api_result["type"])
        if "agentDraw" in api_result:
            self._agent_draw = Draw(api_result["agentDraw"])
        else:
            self.agent_draw = None
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
    def start(self) -> Datetime:
        """
        When the operations starts.
        """
        return self._start

    @property
    def end(self) -> Optional[Datetime]:
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
    def bookmark(self) -> Bookmark:
        """
         The bookmarks for that operation. Only visible to Owner and Operator!
        """
        return self._bookmark

    @property
    def linkplan(self) -> str:
        """
         The draw for that operation. Only visible to Owner and Operator!
        """
        return self._linkplan

    @property
    def keyplan(self) -> str:
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
    def displayOrder(self) -> List:
        """
         Array of task IDs as integers to indicate the order the tasks should
         be displayed in clients.
        """
        return self._displayOrder

    @property
    def glympse(self) -> str:
        """
         The glympse tag for that operation, can be presented on client as a
         link to app: http://glympse.com/!your_group_name
         (always starts with !).
        """
        return self._glympse

    @property
    def statusTag(self) -> str:
        """
         The tag for that operation, to share location in this operation.
        """
        return self._statusTag

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
        self._from_api(self._proxy.get(self._base_url())

    def delete(self):
        """
        Delete this operation.
        Also deletes all tasks, messages and grants.
        """
        self._proxy.delete(self._proxy.get(self._base_url())

    def new_task(self, lat: float, lon: float, todo: TaskType, **params) -> Task:
        """
        Add a new task.
        Requires parameters are location and type.
        Aditional initializing parameters can be set in keyword arguments.
        """
        params["lat"] = lat
        params["lon"] = lon
        params["todo"] = TaskType.value
        api_res = self._proxy.post(self._base_url() + "/task", params)
        return Task(self.proxy, api_res)

    def bulk_new_task(self, tasks: Tuple) -> List[Task]:
        """
        Bulk add new tasks.
        """
        pass

    def get_task(self, id):
        """
        Retrieve specific task.
        """
        return Task(self._proxy(self._base_url() + "/task/" + str(id)))

    def get_tasks(self, **filters):
        """
        Retrieve all task of this operation the user can see.
        Aditional search filters can be queried using the keyword arguments.
        """
        return [Task(api_res) for api_res
                in self._proxy(self._base_url() + "/tasks")]

    def search_tasks(self, lat, lon, km, **filters):
        """
        Find all tasks in a radius of km from lat/lon visible to the user.
        Aditional search filters can be queried using the keyword arguments.
        """
        return [Task(api_res) for api_res
                in self._proxy(self._base_url()
                               + "/tasks/search"
                               + "/" + str(lat)
                               + "/" + str(lon)
                               + "/" + str(km),
                               filters)]

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

    def new_message(self):
        """
        Post message to the op-chat.
        """
        pass

    def get_messages(self, offset=0):
        """
        Retrieve up to 50 messages, add offset to query more
        """
        pass

    def get_message(self, message_id):
        """
        Retrieve a specific message.
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
