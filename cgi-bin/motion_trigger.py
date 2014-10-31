#!/usr/bin/python

from navi import *
import cgi

fields = cgi.FieldStorage()
title = "Motion Trigger"

def reply():

    ret = ""
    ret += "Content-Type: text/html\n\n"
    ret += "<!DOCTYPE html>"
    ret += "<html>"

    ret += default_head(title)
    ret += default_navigator()

    ret += "<body>"
    
    for k in fields.keys():
    	ret += "<div>" + k.upper() + " " + fields[k].value + "</div>"
    
    ret += "</body>"
    ret += "</html>"

    print ret

reply()
