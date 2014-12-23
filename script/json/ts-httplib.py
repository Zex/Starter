#!/usr/bin/env python
#
# ts-httplib.py
#
# Author: Zex <top_zlynch@yahoo.com>
#
import httplib
import json
from os import path, mkdir
from basic import *

if not path.isdir(RESPONSE_DIR):
    mkdir(RESPONSE_DIR)

def case():


    headers = {
        #'Content-Type' : 'application/json'
        #'Content-Type' : 'text/html',
        }

    data = {
            }

    conn = httplib.HTTPConnection(HOST, PORT)

    url = URL# + '/accesspoint'
    conn.request('GET', url, body=json.dumps(data), headers=headers)
    rsp = conn.getresponse()

    with open(RESPONSE_DIR+'/rsp_'+url.replace('/','.')+'.json', 'w') as fd:
        fd.write(str(rsp.msg) + '\n')
        fd.write(str(rsp.read()) + '\n')

    url = URL + '/accesspoint'
    conn.request('GET', url, body=json.dumps(data), headers=headers)
    rsp = conn.getresponse()
    
    with open(RESPONSE_DIR+'/rsp_'+url.replace('/','.')+'.json', 'w') as fd:
        fd.write(str(rsp.msg) + '\n')
        fd.write(str(rsp.read()) + '\n')

    conn.close()
try:
    case()
except Exception as e:
    print e
