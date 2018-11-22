from pyenlone.tasks import *
"""
Basic example of Tasks.
Lists the names of all operations and all tasks in them.

You need to put a valid V apikey in a file called APIKEY.
"""
with open("APIKEY") as apikey:
    T = Tasks(apikey=apikey.read().strip())

print("This are all the operations and all the tasks you can see!: ")
for op in T.get_operations():
    print(op.name)
    for task in op.get_tasks():
        print("\t" + task.name)
