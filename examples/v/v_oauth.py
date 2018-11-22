"""
Example using V OAuth2.
How to get the auth token is beyond this package but you can read some on:
https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#web-application-flow
and
https://v.enl.one/oauth/clients

To run this example, put a valid token with the necesary scopes
in a file called "TOKEN".
"""

from pyenlone import V

with open("TOKEN") as input_file:
    token = input_file.read()[:-1]
v_api = V(token=token)

print(v_api.profile())
print(v_api.googledata())
print(v_api.email().email)
print(v_api.telegram().telegram)
