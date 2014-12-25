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
        'Content-Type' : 'text/plain',
        }

    data = {
            'username' : USERNAME,
            'password' : PASSWORD
            }

    conn = httplib2.Http(".cache")
    """
    url = 'http://localhost/sos/login.html'
    rsp = conn.request(url, 'PUT', body=json.dumps(data), headers=headers)

    headers['Cookie'] = rsp[0]['set-cookie']
    """
    #conn.add_credentials(USERNAME, PASSWORD)
    url = URL
    rsp = conn.request(url, 'GET', body=json.dumps(data), headers=headers)
    #headers['Cookie'] = rsp[0]['set-cookie']

    with open(RESPONSE_DIR+'/rsp_'+url.replace('/','-').replace(':', '_') +'.json', 'w') as fd:
        fd.write('#' + url + '\n' + str(rsp[0]) + '\n')
        fd.write('#' + url + '\n' + str(rsp[1]) + '\n')

    url = URL + '/accesspoint'
    rsp = conn.request(url, 'GET', body=json.dumps(data), headers=headers)
    
    with open(RESPONSE_DIR+'/rsp_'+url.replace('/','-').replace(':', '_') +'.json', 'w') as fd:
        fd.write('#' + url + '\n' + str(rsp[0]) + '\n')
        fd.write('#' + url + '\n' + str(rsp[1]) + '\n')

try:
    case()
except Exception as e:
    print e
