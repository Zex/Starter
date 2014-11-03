#!/usr/bin/env python
#
# cgi-bin/youout.py
# Solution to the YouOut game
#
# Author: zex <top_zlynch@yahoo.com>

import cgi
from navi import *

def youout(total, n):

    cur = 0
    n -= 1
    a = range(1, total+1)

    while len(a) > 1:

        cur = (cur + n) % len(a)
        a.pop(cur)

    return str(a)

if __name__ == '__main__':

    fields = cgi.FieldStorage()
    title = "YouOut!"
   
    ret = "" 
    ret += "Content-Type: text/html\n\n"
    ret += "<!DOCTYPE html>"
    ret += "<html>"
   
    ret += default_head(title)
    ret += default_navigator()
 
    ret += "<body>"
    ret += "<div class=\"content\">"
    
    if fields.has_key('total_player') and fields.has_key('unlucky_n'):

        ret += "<div class=\"normal\">"
        ret += "<label for=total_player><b>Total player: </b></label>"
        ret += "<input type=text name=\"total_player\" readonly=\"true\" value=\""+str(fields['total_player'].value)+"\"/><br>"
        ret += "</div>"
        ret += "<div class=\"normal\">"
        ret += "<label for=\"unlucky_n\"><b>Unlucky N: </b></label>"
        ret += "<input type=text name=\"unlucky_n\" readonly=\"true\" value=\""+str(fields['unlucky_n'].value)+"\"/><br>"
        ret += "</div>"
        ret += "<div class=\"normal\">"
        ret += "<label><b>Lucky Dog: </b><label>"
        ret += "<span><b>" + youout(int(fields['total_player'].value), int(fields['unlucky_n'].value)) + "</b></span><br>"
        ret += "</div>"
  
    else:
        ret += "<span>No parameter given</span>"
 
    ret += "</div>" 
    ret += "</body>"
    ret += "</html>"

    print ret

#if __name__ == '__main__':
#    youout(15, 3)
#    print ":----------------------------------"
#    youout(15, 4)
#    print ":----------------------------------"
#    youout(20, 7)
#    print ":----------------------------------"
#    youout(177, 11)
#    print ":----------------------------------"
#    youout(3, 11)

