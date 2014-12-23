#!/usr/bin/env python
#
# ts-httplib2.py
#
# Author: Zex <top_zlynch@yahoo.com>
#
import httplib2
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

    conn = httplib2.Http()

    url = URL# + '/accesspoint'
    rsp = conn.request(url, 'GET', body=json.dumps(data), headers=headers)

    with open(RESPONSE_DIR+'/rsp_'+url.replace('/','.')+'.json', 'w') as fd:
        fd.write('#headers:\n' + str(rsp[0]) + '\n')
        fd.write('#content:\n' + str(rsp[1]) + '\n')

    url = URL + '/accesspoint'
    rsp = conn.request(url, 'GET', body=json.dumps(data), headers=headers)
    
    with open(RESPONSE_DIR+'/rsp_'+url.replace('/','.')+'.json', 'w') as fd:
        fd.write('#headers:\n' + str(rsp[0]) + '\n')
        fd.write('#content:\n' + str(rsp[1]) + '\n')

try:
    case()
except Exception as e:
    print e
