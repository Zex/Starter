#!/usr/bin/env python
#
# cgi-bin/whereyoulive.py
# Survay of where colleagues live
#
# Author: zex <top_zlynch@yahoo.com>
#
# http://localhost:8080/whereyoulive

import whereyoulive_sum

def survey():

    from cgi import os

    title = "WhereYouLive"
    
    ret = "Content-Type: text/html\n\n"
    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head>"
    ret += "<title>" + title + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<link href=\"/img/badsmile.jpg\" rel=\"icon\" type=\"image/jpg\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head><body>"
    
    ret += "<div class=\"navigator\">"
    ret += "<a name=\"Navigator\"><ul>Navigator</ul></a>"
    ret += "<ul>"
    ret += "<li><a href=\"index#Motions\" title=\"Motions\">Motions</a></li>"
    ret += "<li><a href=\"index#RandomSeq\" title=\"Random Seq\">Random Seq</a></li>"
    ret += "<li><a href=\"index#LeaveMessage\" title=\"Leave a Message\">Leave a Message</a></li>"
    ret += "</ul>"
    ret += "</div>"

    ret += "<div class=\"content\">"

    ret += "<h2>Welcome, " + os.environ["REMOTE_ADDR"] + "!</h2>"
    ret += "<span>" + os.environ["HTTP_USER_AGENT"] + "</span><br><br>"
  
    ret += "<form action=\"whereyoulive.py\" method=\"post\">" 

    for a in whereyoulive_sum.addresses:#preset("../res/Addrs.Sample"):
        ret += "<input type=\"radio\" name=\"addr\" value=\"" + str(a) + "\"/> <b>" + str(a) + "</b><br>"

    ret += "<label for=\"elseaddr\">" + "Somewhere Else ..." + "</label><br>"
    ret += "<input type=\"text\" name=\"elseaddr\"/><br>"
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


