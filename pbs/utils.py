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

    if resp.status != 200:
        raise RuntimeError(f"Status Code: {resp.status}\nReponse:{resp_data}")

    try:
        return json.loads(resp_data)
    except:
        raise RuntimeError(resp_data)


def plainclient(method='GET', path='/', data=None, host='https://pbs.org'):
    req_data = json.dumps(data).encode('utf-8') if data else data

    resp = http.request(
           method, f"{host}{path}",
           body=req_data,
           headers={'Content-Type': 'application/json'})

    resp_data = resp.data.decode('utf-8')

    if resp.status != 200:
        raise RuntimeError(f"Status Code: {resp.status}\nReponse:{resp_data}")

    return resp_data
