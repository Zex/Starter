#!/usr/bin/env python
#
# ts-pycurl.py
#
# Author: Zex <top_zlynch@yahoo.com>
#
import pycurl
#import json
from os import path, mkdir
from basic import *
from StringIO import StringIO

if not path.isdir(RESPONSE_DIR):
    mkdir(RESPONSE_DIR)

def case():

    headers = {
        #'Content-Type' : 'application/json'
        #'Content-Type' : 'text/html',
        }

    data = {
            }

    conn = pycurl.Curl()

    url = 'https://api.github.com/users/Zex/repos'
    connbuf = StringIO()

    conn.setopt(conn.URL, url)
    conn.setopt(conn.WRITEFUNCTION, connbuf.write)
    conn.setopt(conn.HTTPHEADER, [str(x)+':'+str(headers[x]) for x in headers.keys()])
    conn.perform()

    with open(RESPONSE_DIR+'/rsp_'+url.replace('/','.')+'.json', 'w') as fd:
        fd.write('#headers:\n' + connbuf.getvalue() + '\n')

    connbuf.close()

try:
    case()
except Exception as e:
    print e
