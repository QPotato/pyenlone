from datetime import Datetime
from enum import Enum
from typing import Optional, List, Tuple, NewType

from operation import OpID
from v import IGN, GID

TaskID = NewType("TaskID", int)
PortalID = NewType("PortalID", str)


class TaskType(Enum):
    DESRTOY = 1
    CAPTRURE = 2
    FLIP = 4
    LINK = 8
    KEYFARM = 9
    MEET = 10
    RECHARGE = 11
    UPGRADE = 12
    OTHER = 99


class TaskStatus(Enum):
    PENDING = 1
    ACKNOWLEDGE = 2
    DONE = 3
    OTHER = 99


class LinkTarget:
    def __init__(self, api_result):
        self.name = api_result["name"]
        self.portal_id = PortalID(api_result["portalID"])
        self.lat = api_result["lat"]
        self.lon = api_result["lon"]


class Task:
    def __init__(self, api_result):
        self._id = api_result["id"]
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
        self._start = Datetime(api_result["start"])
        if "end" in api_result:
            self._end = Datetime(api_result["end"])
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
        self._created_at = Datetime(api_result["createdAt"])
        self._updated_at = Datetime(api_result["updatedAt"])
        if "accepted" in api_result:
            self._accepted = [(IGN(ign), Datetime(dt))
                              for (ign, dt) in api_result["accepted"]]
        else:
            self._accepted = None
        if "done" in api_result:
            self._done = [(GID(ign), Datetime(dt))
                          for (ign, dt) in api_result["done"]]
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
            apires_to_task_status = {
                "pending": TaskStatus.PENDING,
                "acknowledge": TaskStatus.ACKNOWLEDGE,
                "done": TaskStatus.DONE
            }
            self._status = apires_to_task_status[api_result["status"]]
        else:
            self._status = None
        if "portalImage" in api_result:
            self.portal_image = api_result["portalImage"]
        else:
            self._portal_image = None

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
    def owner(self) -> IGN:
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
    def start(self) -> Datetime:
        """
        The date and Time when it starts.
        """
        return self._start

    @property
    def end(self) -> Optional[Datetime]:
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
    def created_at(self) -> Datetime:
        """
         When it was created.
        """
        return self._created_at

    @property
    def updated_at(self) -> Datetime:
        """
         When it was updated.
        """
        return self._updated_at

    @property
    def accepted(self) -> Optional[List[Tuple(IGN, Datetime)]]:  # CHECKEAR
        """
         Who accepted this task.
        """
        return self._accepted

    @property
    def done(self) -> Optional[List[Tuple(IGN, Datetime)]]:  # CHECKEAR
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
