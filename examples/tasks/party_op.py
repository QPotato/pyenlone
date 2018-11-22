"""
Example showing how to create operations, create tasks and assign them.
"""
from datetime import datetime

from pyenlone.tasks import Tasks, OpType, TaskType
from pyenlone.v import V

with open("APIKEY") as apikey:
    ak = apikey.read().strip()
    T = Tasks(apikey=ak)
    V = V(apikey=ak)

# Get your V info.
you = V.whoami()
# Create an operation for your party
party = T.new_operation("My birthday party operation", OpType.OTHER)
# updrade, get it?
celebration = party.new_task("Celebrate at my house!",
                             you.lat,
                             you.lon,
                             TaskType.UPGRADE)
# You may want to pick another VTeam here.
your_friends = V.list_teams()[0]
party.grant([{"type": "vteam",
              "id": your_friends.teamid,
              "permission": "m"}])
celebration.assign([{"type": "vteam", "id": your_friends.teamid}])
msg = party.send_message({"message": "Bring booze and XMPs!"})

# Oh no, you forgot to set the date for the party!
celebration.start = datetime(2025, 12, 25)
# Always save changes to post it to Tasks servers.
celebration.save()
party.edit_message(msg["id"],
                   {"message": "Bring booze, XMPs and Santa hats!"})
input("Check out your party on RAID and then press enter to delete it.")
party.delete()
