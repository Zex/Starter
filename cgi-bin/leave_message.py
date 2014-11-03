#!/usr/bin/python

import cgi
from redis import Connection
from socket import gethostname
from navi import *

fields = cgi.FieldStorage()
title = "Message Box"
msg_prefix = 'custom.message.'

def insert_msg(cust, tm, msg):

    conn = Connection(host=gethostname(),port=6379)
    conn.send_command('set', msg_prefix+cust+'--'+tm, msg)

    conn.disconnect()

def read_msg():

    ret = ''

    conn = Connection(host=gethostname(),port=6379)
    conn.send_command('keys', msg_prefix+'*')
    keys = conn.read_response()
    vals = []

    if len(keys) != 0:
        conn.send_command('mget', *keys)
        vals = conn.read_response()

        ret += "<h2>" + "Message log" + "</h2>"

        for k, v in zip(keys, vals):
            ret += "<span>" + k.replace(msg_prefix, '').replace('--', ' ') + "</span>"
            ret += "<pre readonly=\"true\">" + v + "</pre>"

    conn.disconnect()
    ret += "<br>"

    return ret

def reply():

    import time, os

    ret = ""
    ret += "Content-Type: text/html\n\n"
    ret += "<!DOCTYPE html>"
    ret += "<html>"
 
    ret += default_head(title)
    ret += default_navigator()
 
    ret += "<body>"
    ret += "<div class=\"content\">"
    ret += "<h2>Welcome, " + os.environ["REMOTE_ADDR"] + "!</h2>"
    ret += "<span>" + os.environ["HTTP_USER_AGENT"] + "</span><br><br>"
 
    if fields.has_key('msgbox'):
        insert_msg(os.environ["REMOTE_ADDR"], time.strftime(time.asctime()), fields['msgbox'].value)
 
    ret += read_msg()
 
    ret += "</div>"
    ret += "</body>"
    ret += "</html>"

    print ret

reply()

