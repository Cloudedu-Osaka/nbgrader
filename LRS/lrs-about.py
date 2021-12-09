#!/usr/bin/env python
# coding: utf-8

import requests
from requests.exceptions import Timeout
import json
#from tornado.httpclient import HTTPClient, AsyncHTTPClient, HTTPError
#import asyncio



headers = {
    'X-Experience-API-Version': '1.0.3',
    'Content-Type': 'application/json; charset=utf-8'
}
auth=('9efbfc629a314c67985176db789ef6093aaff2b8', 'a3abd823e96b283a622167040bbd13e3e33edfa7')

try:
    response = requests.get('http://localhost:8081/data/xAPI/about', headers=headers, auth=auth, timeout=3.0)
except Timeout:
    pass
else:
    print(response.text)
    try:
        response = requests.post('http://localhost:8081/data/xAPI/statements', data={}, headers=headers, auth=auth, timeout=3.0)
    except Timeout:
        pass
    else:
        print(response.text)

#async def f():
#    http_client = AsyncHTTPClient()
#    try:
#        response = await http_client.fetch('http://localhost:8081/data/xAPI/about', headers=headers, method='GET', auth_username='9efbfc629a314c67985176db789ef6093aaff2b8', auth_password='a3abd823e96b283a622167040bbd13e3e33edfa7')
#    except Exception as e:
#        print("Error: %s" % e)
#    else:
#        print(response.body)

#asyncio.run(f())
#print('end')
#loop = asyncio.get_event_loop()
#loop.run_until_complete(f())