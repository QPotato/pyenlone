"""
Example using the banned API.

To run this example, put a valid token with the necesary scopes
in a file called "TOKEN".
"""
from pyenlone import V, banned

with open("TOKEN") as input_file:
    token = input_file.read()[:-1]
v_api = V(token=token)
my_google_id = v_api.googledata().gid

if banned(my_google_id):
    print("Yeah sure, blame it on your ISP :)")
else:
    print("All good!")
