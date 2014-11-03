#!/usr/bin/env python

def default_navigator():

    ret = ""
    ret += "<div class=\"navigator\">"
    ret += "<a name=\"Navigator\"><ul>Navigator</ul></a>"
    ret += "<ul>"
    ret += "<li><a href=\"starter.py#YouOut\" title=\"You Out\">You Out</a></li>"
    ret += "<li><a href=\"starter.py#Motions\" title=\"Motions\">Motions</a></li>"
    ret += "<li><a href=\"starter.py#RandomSeq\" title=\"Random Seq\">Random Seq</a></li>"
    ret += "<li><a href=\"starter.py#LeaveMessage\" title=\"Leave a Message\">Leave a Message</a></li>"
    ret += "</ul>"
    ret += "</div>"
    return ret

def default_head(title = ""):

    ret = ""
    ret += "<head>"
    ret += "<title>" + title + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<link href=\"/img/badsmile.jpg\" rel=\"icon\" type=\"image/jpg\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head>"

    return ret
