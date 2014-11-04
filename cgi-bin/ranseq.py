#!/usr/bin/env python
#
# ranseq.py
# Author: Zex <top_zlynch@yahoo.com>

from random import randint#, choice
from string import digits
from navi import *

def ranseq(length):
#    ret += "--------------------------------------------------------->"
#    ancient_a = [int(choice(digits)) for i in xrange(int(length))]
#    ancient_b = [int(choice(digits)) for i in xrange(int(length))]
    ancient_a = [randint(1, 1000) for i in xrange(int(length))]
    ancient_b = [randint(1, 1000) for i in xrange(int(length))]

    ret = ""
    ret += "<table class=\"content\">"
    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">Ancient a: </td><td class=\"normal\"><span contenteditable=\"false\">" + str(ancient_a) + "</span></td>"
    ret += "</tr>"
    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">Ancient b: </td><td class=\"normal\"><span contenteditable=\"false\">" + str(ancient_b) + "</span></td>"
    ret += "</tr>"

    ancient_a.extend(ancient_b)
    ancient_a.sort()

    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">Ancient a: </td><td class=\"normal\"><span contenteditable=\"false\">" + str(ancient_a) + "</span></td>"
    ret += "</tr>"

    child_min = ancient_a[:(len(ancient_a)-2)/2]
    child_max = ancient_a[(len(ancient_a)-2)/2:-2]

    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">child_min: </td><td class=\"normal\"><span contenteditable=\"false\">" + str(child_min) + "</span></td>"
    ret += "</tr>"
    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">child_max: </td><td class=\"normal\"><span contenteditable=\"false\">" + str(child_max) + "</span></td>"
    ret += "</tr>"

    child_min.append(ancient_a[-1])
    child_max.append(ancient_a[-2])

    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">child_min sum: </td><td class=\"normal\"><span contenteditable=\"false\">" + str(reduce(lambda x,y:x+y, child_min)) + "</span></td>"
    ret += "</tr>"
    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">child_max sum: </td><td class=\"normal\"><span contenteditable=\"false\">" + str(reduce(lambda x,y:x+y, child_max)) + "</span></td>"
    ret += "</tr>"
    ret += "</table>"
#    ret += "---------------------------------------------------------+"
    return ret

def reply():
    import cgi
    title = "Random Seq"
   
    ret  = ""
    ret += "Content-Type: text/html\n\n"
    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += default_head(title) 
    ret += default_navigator() 

    ret += "<body>"
    ret += "<div class=\"content\">"
   
    for i in [100, 10, 1000, 999, 3]:
        ret += "<h2>" + "Ranseq with " + str(i) + "</h2>"
        ret += ranseq(i)

   
    ret += "</div>" 
    ret += "</body>"
    ret += "</html>"

    print ret

reply()
