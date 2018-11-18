from datetime import Datetime
from typing import NewType

MessageID = NewType("MessageID", int)


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
        """
         The message id.
        """
        return self._id

    @property
    def message(self):
        """
         The message you want to send.
        """
        return self._message

    @property
    def reply_to(self):
        """
         The message id you want reply to.
        """
        return self._reply_to

    @property
    def time(self):
        """
         The time the message were created.
        """
        return self._time

    @property
    def edit_time(self):
        """
         The time the message were updated.
        """
        return self._edit_time
