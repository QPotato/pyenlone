from datetime import datetime
from enum import Enum
from typing import Optional, List, NewType

from ..v import GID

OpID = NewType("OpID", int)
TaskID = NewType("TaskID", int)
PortalID = NewType("PortalID", str)


def _fix_task_params(params):
    if "todo" in params:
        params["todo"] = params["todo"].value
    if "portal_id" in params:
        params["portalID"] = params["portal_id"]
    if "link_target" in params:
        params["linkTarget"] = params["link_target"]
        if type(params["linkTarget"]) is dict:
            params["linkTarget"] = [params["linkTarget"]]
    if "group_name" in params:
        params["groupName"] = params["group_name"]
    if "portal_image" in params:
        params["portalImage"] = params["portal_image"]


class TaskType(Enum):
    DESTROY = 1
    CAPTRURE = 2
    FLIP = 4
    LINK = 8
    KEYFARM = 9
    MEET = 10
    RECHARGE = 11
    UPGRADE = 12
    OTHER = 99


class TaskStatus(Enum):
    PENDING = "pending"
    ACKNOWLEDGE = "acknowledge"
    DONE = "done"


class LinkTarget:
    def __init__(self, api_result):
        # api_result = json.loads(api_result)
        self.name = api_result["name"]
        self.portal_id = PortalID(api_result["portalID"])
        self.lat = api_result["lat"]
        self.lon = api_result["lon"]

    def to_api(self):
        return {
            "name": self.name,
            "portalID": self.portal_id,
            "lat": self.lat,
            "lon": self.lon
        }


class Task:
    def __init__(self, proxy, api_result):
        self._proxy = proxy

        self._id = api_result["id"]
        self._from_api(api_result)

    def _from_api(self, api_result):
        self._op = OpID(api_result["op"])
        if "name" in api_result:
            self._name = api_result["name"]
        else:
            self._name = None
        self._owner = api_result["owner"]
        self._lat = api_result["lat"]
        self._lon = api_result["lon"]
        if "portal" in api_result:
            self._portal = api_result["portal"]
        else:
            self._portal = None
        if "portalID" in api_result:
            self._portal_id = PortalID(api_result["portalID"])
        else:
            self._portal_id = None
        if "comment" in api_result:
            self._comment = api_result["comment"]
        else:
            self._comment = None
        self._start = datetime.fromtimestamp(api_result["start"] / 1000)
        if "end" in api_result:
            self._end = datetime.fromtimestamp(api_result["end"] / 1000)
        else:
            self._end = None
        if "previous" in api_result:
            self._previous = TaskID(api_result["previous"])
        else:
            self._previous = None
        if "alternative" in api_result:
            self._alternative = TaskID(api_result["alternative"])
        else:
            self._alternative = None
        if "priority" in api_result:
            self._priority = api_result["priority"]
        else:
            self._priority = None
        if "repeat" in api_result:
            self._repeat = api_result["repeat"]
        else:
            self._repeat = None
        self._todo = TaskType(api_result["todo"])
        if "linkTarget" in api_result:
            self._link_target = [LinkTarget(ar)
                                 for ar in api_result["linkTarget"]]
        else:
            self._link_target = None
        self._created_at = datetime.fromtimestamp(api_result["createdAt"] / 1000)
        self._updated_at = datetime.fromtimestamp(api_result["updatedAt"] / 1000)
        if "accepted" in api_result:
            self._accepted = [(GID(ar["user"]), datetime.fromtimestamp(ar["time"] / 1000))
                              for ar in api_result["accepted"]]
        else:
            self._accepted = None
        if "done" in api_result:
            self._done = [(GID(ar["user"]), datetime.fromtimestamp(ar["time"] / 1000))
                          for ar in api_result["done"]]
        else:
            self._done = None
        if "assigned" in api_result:
            self._assigned = [GID(gid) for gid in api_result["assigned"]]
        else:
            self._assigned = None
        if "groupName" in api_result:
            self._group_name = api_result["groupName"]
        else:
            self._group_name = None
        if "status" in api_result:
            self._status = TaskStatus(api_result["status"])
        else:
            self._status = None
        if "portalImage" in api_result:
            self.portal_image = api_result["portalImage"]
        else:
            self._portal_image = None

        def _to_api(self):
            return {
                "name": self._name,
                "lat": self._lat,
                "lon": self._lon,
                "portal": self._portal,
                "portalID": self._portal_id,
                "start": self._start.timestamp() * 1000,
                "end": self._end.timestamp() * 1000 if self._end else None,
                "comment": self._comment,
                "previous": self._previous,
                "alternative": self._alternative,
                "priority": self._priority,
                "repeat": self._repeat,
                "todo": self._todo.value,
                "linkTarget": [lt.to_api() for lt
                               in self._link_target.to_api()]
                              if self._link_target else None,
                "createdAt": self._created_at,
                "updatedAt": self._updated_at,
                "accepted": self._accepted,
                "done": [{"user": dn[0], "time": dn[1]}
                         for dn in self._done] if self._done else None,
                "assigned": self._assigned,
                "groupName": self._group_name,
                "status": self._status,
                "portalimage": self._portal_image,
            }

    @property
    def id(self) -> TaskID:
        """
         Id of this task. Unique inside of an operation.
        """
        return self._id

    @property
    def op(self) -> OpID:
        """
         ID of the Operation this task belongs to.
        """
        return self._op

    @property
    def name(self) -> Optional[str]:
        """
         Name of that task.
        """
        return self._name

    @property
    def owner(self) -> GID:
        """
         Google ID.
        """
        return self._owner

    @property
    def lat(self) -> float:
        """
        Latitude.
        """
        return self._lat

    @property
    def lon(self) -> float:
        """
        Longitude.
        """
        return self._lon

    @property
    def portal(self) -> Optional[str]:
        """
         Name of the Portal targeted in the task.
        """
        return self._portal

    @property
    def portal_id(self) -> Optional[PortalID]:
        """
         ID (guid) of the Portal targeted in the task.
        """
        return self._portal_id

    @property
    def start(self) -> datetime:
        """
        The date and Time when it starts.
        """
        return self._start

    @property
    def end(self) -> Optional[datetime]:
        """
        The date and Time when it ends.
        """
        return self._end

    @property
    def comment(self) -> Optional[str]:
        """
         A comment for the agent to read.
        """
        return self._comment

    @property
    def previous(self) -> Optional[TaskID]:
        """
         If this task needs another task to be completed before.
        """
        return self._previous

    @property
    def alternative(self) -> Optional[TaskID]:
        """
         If this task is an alternative to another task.
        """
        return self._alternative

    @property
    def priority(self) -> Optional[int]:
        """
         How important this task is (1 is most important).
        """
        return self._priority

    @property
    def repeat(self) -> Optional[int]:
        """
         How often should this task be done?
        """
        return self._repeat

    @property
    def todo(self) -> TaskType:
        """
         What should be done?
        """
        return self._todo

    @property
    def link_target(self) -> Optional[List[LinkTarget]]:  # CHECKEAR
        """
         If this is a task to link somewhere, give the name and coordinates of
         the portal(s) to link to.
        """
        return self._link_target

    @property
    def created_at(self) -> datetime:
        """
         When it was created.
        """
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        """
         When it was updated.
        """
        return self._updated_at

    @property
    def accepted(self) -> Optional[List]:  # CHECKEAR
        """
         Who accepted this task.
        """
        return self._accepted

    @property
    def done(self) -> Optional[List]:  # CHECKEAR
        """
         Who completed this task.
        """
        return self._done

    @property
    def assigned(self) -> Optional[List[GID]]:  # CHECKEAR
        """
        If that task is assigned to a single agent.
        """
        return self._assigned

    @property
    def group_name(self) -> Optional[str]:
        """
         If that task meant for a group of agents.
        """
        return self._group_name

    @property
    def status(self) -> Optional[TaskStatus]:
        """
        TaskStatus of this task. Set by backend for specific actions.
        PENDING after creation.
        ACKNOWLEDGE after the task was accepted by an agent and current status
        was pending.
        DONE after the task was marked as done.
        """
        return self._status

    @property
    def portal_image(self):
        """
         Image url for portal.
        """
        return self._portal_image

    @name.setter
    def name(self, value):
        self._name = value

    @lat.setter
    def lat(self, value):
        self._lat = value

    @lon.setter
    def lon(self, value):
        self._lon = value

    @portal.setter
    def portal(self, value):
        self._portal = value

    @portal_id.setter
    def portal_id(self, value):
        self._portal_id = PortalID(value)

    @start.setter
    def start(self, value: datetime):
        self._start = value

    @end.setter
    def end(self, value: datetime):
        self._end = value

    @comment.setter
    def comment(self, value):
        self._comment = value

    @previous.setter
    def previous(self, value):
        self._previous = TaskID(value)

    @alternative.setter
    def alternative(self, value):
        self._alternative = TaskID(value)

    @priority.setter
    def priority(self, value):
        self._priority = value

    @repeat.setter
    def repeat(self, value):
        self._repeat = value

    @todo.setter
    def todo(self, value: TaskType):
        self._todo = value

    @assigned.setter
    def assigned(self, value):
        self._assigned = value

    @group_name.setter
    def group_name(self, value):
        self._group_name = value

    @status.setter
    def status(self, value: TaskStatus):
        self._status = value

    @portal_image.setter
    def portal_image(self, value):
        self._portal_image = value

    def _base_url(self):
        return "/op/" + str(self.op) + "/task/" + str(self.id)

    def save(self):
        """
        Save changes to Tasks server.
        """
        self._proxy.put(self._base_url(), self._to_api())

    def update(self):
        """
        Update data from Tasks servers.
        """
        self._from_api(self._proxy.get(self._base_url()))

    def delete(self):
        """
        Delete this task.
        Also deletes task specific grants.
        """
        self._proxy.delete(self._base_url())

    def add_grant(self):
        """
        Grant permission on this task.
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

    def accept(self):
        """
        User accepts this task.
        """
        self._proxy.post(self._base_url() + "/acknowledge")

    def decline(self):
        """
        User who accepted this task declines it afterwards.
        """
        self._proxy.delete(self._base_url() + "/acknowledge")

    def acknowledge(self):
        """
        User who accepted this task.
        """
        self._proxy.get(self._base_url() + "/acknowledge") # TODO: checkear si podemos devolver un Agent aca

    def set_complete(self):
        """
        User has completed this task.
        """
        self._proxy.post(self._base_url() + "/complete")

    def get_complete(self):
        """
        User who completed this task.
        """
        self._proxy.get(self._base_url() + "/complete") # TODO: checkear si podemos devolver un Agent aca

    def assign(self):
        """
        Assign this task to a user or list of users.
        """
        self._proxy.post(self._base_url() + "/assigned")

    def unassign(self):
        """
        Unassign task.
        """
        self._proxy.post(self._base_url() + "/assigned")
