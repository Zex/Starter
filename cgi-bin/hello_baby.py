#!/usr/bin/python

import cgi
from navi import *

fields = cgi.FieldStorage()
title = "Hello Baby"

def reply():

    ret = ""

    ret += "Content-Type: text/html\n\n"
    ret += "<!DOCTYPE html>"
    ret += "<html>"

    ret += default_head(title)
    ret += default_navigator()

    ret += "<body>"
    ret += "<div class=\"content\">"

    for k in fields.keys():
	    ret += "<div>" + k + " => " + fields[k].value + "</div>"

    ret += "</div>"
    ret += "</body>"
    ret += "</html>"

    print ret

reply()
