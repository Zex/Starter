#!/usr/bin/env python
#
# ts-urllib2.py
#
# Author: Zex <top_zlynch@yahoo.com>
#
import urllib2
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

#    url = 'http://' + '127.0.0.1:5000'#/sos/login.html'
#    auth = urllib2.HTTPPasswordMgrWithDefaultRealm()
#    auth.add_password(None, url, USERNAME, PASSWORD)
#    auth_handler = urllib2.HTTPBasicAuthHandler(auth)
#
#    opener = urllib2.build_opener(auth_handler)
#    urllib2.install_opener(opener)
#    for k in headers.items():
#        opener.addheaders.append(k)
#    rsp = opener.open(url, json.dumps(data))
#    with open(RESPONSE_DIR+'/rsp_'+url.replace('/','')+'.json', 'w') as fd:
#        print rsp
#
#    opener.close()

    url = URL# + '/accesspoint'
    req = urllib2.Request(url, json.dumps(data), headers)
    req.get_method = lambda:'GET'
    rsp = urllib2.urlopen(req)

    with open(RESPONSE_DIR+'/rsp_'+url.replace('/','-').replace(':', '_') +'.json', 'w') as fd:
        fd.write('#' + url + '\n' + str(rsp.headers) + '\n' + rsp.read() + '\n')

try:
    case()
except Exception as e:
    print e
