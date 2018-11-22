from pyenlone.tasks import TaskStatus, Tasks
from pyenlone.v import V

with open("APIKEY") as apikey:
    ak = apikey.read().strip()
    T = Tasks(apikey=ak)
    V = V(apikey=ak)

loc = V.location(V.whoami().enlid)
ops = T.search_operations(loc["lat"], loc["lon"], loc["distance"])

print("Bored? Here are some things you can do to help your faction!:")
for op in ops:
    for task in op.get_tasks():
        if task.status == TaskStatus.PENDING:
            print(task.name)
            print("\t" + task.maps_link)
            print("\t" + task.intel_link)
            task_owner = V.trust(task.owner).agent
            print("\t Contact: " + task_owner)
