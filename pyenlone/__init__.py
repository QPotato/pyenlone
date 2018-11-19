"""
Implements enl.one APIs:
- v.enl.one
- tasks.enl.one (Soon)
- status.enl.one (Not very soon, but soon)
For more info: https://wiki.enl.one/doku.php?id=start
"""
from .v import V, banned, Agent, DetailAgent, GID, IGN, Team, TeamID, TeamRole, TeamMember
from .tasks import Tasks, Operation, OpType, OpID, Task, TaskID, PortalID, Message, MessageID, Grant
from .enloneexception import EnlOneException

NAME = "pyenlone"
