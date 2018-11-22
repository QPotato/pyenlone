"""
Example using agent location to create a google maps link.

To run this example, put a valid token with the necesary scopes
in a file called "TOKEN".
"""

from pyenlone import V

with open("TOKEN") as input_file:
    token = input_file.read()[:-1]
v = V(token=token)

loc = v.location(v.profile().enlid)
print("You are at https://google.com/maps?ll=%s,%s !" % (loc.lat, loc.lon))
