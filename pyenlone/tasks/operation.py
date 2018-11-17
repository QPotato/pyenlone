from enum import Enum
from datetime import Datetime
from typing import Optional, List, Dict
from ..types import OpID, IGN, Draw, Bookmark, LatLng


class OpType(Enum):
    FIELD = 0
    FIELD_DEFENSE = 1
    AREA = 2
    LINKSTAR = 3
    LINKART = 4
    OTHER = 5


class Operation:
    def __init__(self, api_result):
        self._id = OpID(api_result["id"])
        self._name = IGN(api_result["name"])
        self._owner = api_result["owner"]
        self._start = Datetime(api_result["start"])
        if "end" in api_result:
            self._end = Datetime(api_result["end"])
        else:
            self._end = None
        apires_to_optype = {
            "field": OpType.FIELD,
            "field-defende": OpType.FIELD_DEFENSE,
            "area": OpType.AREA,
            "linkstar": OpType.LINKSTAR,
            "linkart": OpType.LINKART,
            "other": OpType.OTHER,
        }
        self._type = apires_to_optype[api_result["type"]]
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
        return self._id

    @property
    def name(self) -> Optional[str]:
        return self._name

    @property
    def owner(self) -> IGN:
        return self._owner

    @property
    def start(self) -> Datetime:
        return self._start

    @property
    def end(self) -> Optional[Datetime]:
        return self._end

    @property
    def type(self) -> OpType:
        return self._type

    @property
    def agent_draw(self) -> Draw:
        return self._agent_draw

    @property
    def draw(self) -> Draw:
        return self._draw

    @property
    def bookmark(self) -> Bookmark:
        return self._bookmark

    @property
    def linkplan(self) -> str:
        return self._linkplan

    @property
    def keyplan(self) -> str:
        return self._keyplan

    @property
    def opsbf_settings(self) -> str:
        return self._opsbf_settings

    @property
    def opsbf_save(self) -> str:
        return self._opsbf_save

    @property
    def other(self) -> Dict:
        return self._other

    @property
    def displayOrder(self) -> List:
        return self._displayOrder

    @property
    def glympse(self) -> str:
        return self._glympse

    @property
    def statusTag(self) -> str:
        return self._statusTag

    @property
    def ne(self) -> LatLng:
        return self._ne

    @property
    def nw(self) -> LatLng:
        return self._nw

    @property
    def se(self) -> LatLng:
        return self._se

    @property
    def sw(self) -> LatLng:
        return self._sw
