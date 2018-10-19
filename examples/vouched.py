"""
Example that uses distance method to determine if you vouched the author of
this package.

To run this example, put a valid API Key ona file called "APIKEY".
"""

from pyenlone import V

with open("APIKEY") as input_file:
    apikey = input_file.read()[:-1]
v_api = V(apikey=apikey)

your_enlid = v_api.whoami().enlid
author_enlid = v_api.search_one(query="QuanticPotato").enlid
if len(v_api.distance(your_enlid, author_enlid)) == 2:
    print("You vouched the author of the package.")
else:
    print("You did not vouch the author of this package")
