#!/usr/bin/env python3

import urllib3, json

http = urllib3.PoolManager()

def client(method='GET', path='/', data=None, host='https://pbs.org'):
    req_data = json.dumps(data).encode('utf-8') if data else data

    resp = http.request(
           method, f"{host}{path}",
           body=req_data,
           headers={'Content-Type': 'application/json'})

    resp_data = resp.data.decode('utf-8')
    resp_status = resp.status

    return resp_status, resp_data
