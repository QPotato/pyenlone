from datetime import Datetime
from ..types import MessageID


class Message:
    def __init__(self, api_res):
        self._id = MessageID(api_res["id"])
        self._message = api_res["message"]
        if "replyTo" in api_res:
            self._reply_to = Message(api_res["replyTo"])
        else:
            self._reply_to = None
        # CHECKEAR esto dice algo de timestamp
        self._time = Datetime(api_res["time"])
        if "editTime" in api_res:
            # CHECKEAR esto dice algo de timestamp
            self._edit_time = Datetime(api_res["editTime"])
        else:
            self._edit_time = None

    @property
    def id(self):
        return self._id

    @property
    def message(self):
        return self._message

    @property
    def time(self):
        return self._time

    @property
    def edit_time(self):
        return self._edit_time
