from pyenlone.tasks import *
from pyenlone.v import *

with open("APIKEY") as apikey:
    ak = apikey.read().strip()
    T = Tasks(apikey=ak)
    V = V(apikey=ak)

your_google_id = V.whoami().gid

ops = []
for op in T.get_operations():
    for task in op.get_tasks():
        for com in task.done:
            if com["user"] == your_google_id and op not in ops:
                print(op.name)
                ops.append(op)
print("Whoa! You helped in all of this operations? You are awesome!")
