from enum import Enum
from typing import Union, NewType
from ..v import RoleType, GID, TeamID, VLevel

Permission = NewType("Permission", str)
RocksApikey = NewType("RocksApikey", int)


class GrantType(Enum):
    USER = "user"
    VTEAM = "vteam"
    ROCKS = "rocks"
    VLEVEL = "vlevel"
    ROCKSEVENT = "rocksevent"

class PermissionType(Enum):
    MEMBER = "m"
    READ = "r"
    WRITE = "w"
    

class Grant:
    def __init__(self, api_res):
        self._type = GrantType(api_res["type"])
        if self._type == GrantType.USER:
            self._id = GID(api_res["id"])
        elif self.type == GrantType.VTEAM:
            self._id = TeamID(api_res["id"])
        elif self.type == GrantType.ROCKS or GrantType.ROCKSEVENT:
            self._id = RocksApikey(api_res["id"])
        elif self.type == GrantType.VLEVEL:
            self._id = VLevel(api_res["id"])
        self._permission = Permission(api_res["permission"])

        if "role" in api_res:
            if self.type == GrantType.VTEAM:
                self._role = RoleType(api_res["role"])
            else:
                self._role = api_res["role"]
        else:
            self._role = None

        if "team" in api_res:
            self._team = api_res["team"]
        else:
            self._team = None

        @property
        def type(self) -> GrantType:
            """
            Type of the grant.
            """
            return self._type

        @property
        def id(self) -> Union(GID, TeamID, RocksApikey, VLevel):
            """
            The string describing the object that is granted access.
            """
            return self._id

        @property
        def permission(self) -> Permission:
            """
            What kind of access.
            """
            return self._permission

        @property
        def role(self) -> Union(RoleType, str):
            """
            Role/Sub group of the team.
            """
            return self._role

        @property
        def team(self) -> int:
            """
            Rocksevent Team ID.
            """
            return self._team
