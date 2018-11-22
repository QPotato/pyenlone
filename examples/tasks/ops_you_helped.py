"""
To run this example, you need to put a VOAuth token with "google" scope in
a file called "TOKEN".
"""
from pyenlone.tasks import Tasks
from pyenlone.v import V

with open("TOKEN") as token:
    tk = token.read().strip()
    T = Tasks(voauth=tk)
    V = V(token=tk)

your_google_id = V.googledata()["gid"]

ops = []
for op in T.get_operations():
    for task in op.get_tasks():
        for com in task.done:
            if com["user"] == your_google_id and op not in ops:
                print(op.name)
                ops.append(op)
print("Whoa! You helped in all of this operations? You are awesome!")
