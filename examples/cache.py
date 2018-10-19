"""
Example using cache.

To run this example, put a valid token with the necesary scopes
in a file called "TOKEN".
"""

from pyenlone import V

with open("TOKEN") as input_file:
    token = input_file.read()[:-1]
v_api = V(token=token, cache=5)
for i in range(10):
    print(v_api.profile())
