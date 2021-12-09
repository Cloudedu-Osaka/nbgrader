#!/usr/bin/env python
# coding: utf-8

import pprint
import requests
from requests.exceptions import Timeout
import json

auth=('9efbfc629a314c67985176db789ef6093aaff2b8', 'a3abd823e96b283a622167040bbd13e3e33edfa7')
response = requests.get('''http://localhost:3000/api/statements/aggregate?cache=false&maxTimeMS=5000&maxScan=10000&pipeline=[{"$match": {"timestamp" : {"$lte": {"$dte": "2021-12-08T06:09:55.343Z"}}}}]''', auth=auth, timeout=3.0)

res = json.loads(response.text)
#print(json.dumps(response.text, indent=4))

for r in res:
    print(r['statement'])
    r2 = requests.delete('http://localhost:3000/api/v2/statement/'+r['_id'],auth=auth, timeout=3.0)
    print(r2.text)