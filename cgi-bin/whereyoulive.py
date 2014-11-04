#!/usr/bin/env python
#
# cgi-bin/whereyoulive.py
# Survay of where colleagues live
#
# Author: zex <top_zlynch@yahoo.com>
#
# http://localhost:8080/whereyoulive

from navi import *
import whereyoulive_sum

def survey():

    from cgi import os

    ret = "Content-Type: text/html\n\n"
    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += default_head("Where You Live") 
    ret += default_navigator() 

    ret += "<body>"
    ret += "<div class=\"content\">"

    ret += "<h2>Welcome, " + os.environ["REMOTE_ADDR"] + "!</h2>"
    ret += "<span>" + os.environ["HTTP_USER_AGENT"] + "</span><br><br>"
  
    ret += "<form action=\"whereyoulive.py\" method=\"post\">" 

    for a in whereyoulive_sum.addresses:#preset("../res/Addrs.Sample"):
        ret += "<input type=\"radio\" name=\"addr\" value=\"" + str(a) + "\"/> <b>" + str(a) + "</b><br>"

    ret += "<br>"
    ret += "<label for=\"elseaddr\">" + "Somewhere Else ..." + "</label><br>"
    ret += "<input type=\"text\" name=\"elseaddr\"/><br>"

    ret += "<br><br>"
    ret += "<input type=\"submit\" value=\"" + "Submit" + "\"/>"
    ret += "</form>"

    ret += "</div>" 
    ret += "</body>"
    ret += "</html>"

    return ret

def reply():

    from cgi import FieldStorage

    kwargs = FieldStorage()

    if kwargs.has_key('addr') or kwargs.has_key('elseaddr'):
        return whereyoulive_sum.reply(kwargs)
    else:
        return survey()

if __name__ == '__main__':
    print reply()


