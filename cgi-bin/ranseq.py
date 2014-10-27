#!/usr/bin/env python
#
# ranseq.py
# Author: Zex <top_zlynch@yahoo.com>

from random import randint#, choice
from string import digits

def ranseq(length):
#    print "--------------------------------------------------------->"
#    ancient_a = [int(choice(digits)) for i in xrange(int(length))]
#    ancient_b = [int(choice(digits)) for i in xrange(int(length))]
    ancient_a = [randint(1, 1000) for i in xrange(int(length))]
    ancient_b = [randint(1, 1000) for i in xrange(int(length))]

    print "<tr>"
    print "<td>Ancient a: </td><td><span contenteditable=\"false\">" + str(ancient_a) + "</span></td>"
    print "</tr>"
    print "<tr>"
    print "<td>Ancient b: </td><td><span contenteditable=\"false\">" + str(ancient_b) + "</span></td>"
    print "</tr>"

    ancient_a.extend(ancient_b)
    ancient_a.sort()

    print "<tr>"
    print "<td>Ancient a: </td><td><span contenteditable=\"false\">" + str(ancient_a) + "</span></td>"
    print "</tr>"

    child_min = ancient_a[:(len(ancient_a)-2)/2]
    child_max = ancient_a[(len(ancient_a)-2)/2:-2]

    print "<tr>"
    print "<td>child_min: </td><td><span contenteditable=\"false\">" + str(child_min) + "</span></td>"
    print "</tr>"
    print "<tr>"
    print "<td>child_max: </td><td><span contenteditable=\"false\">" + str(child_max) + "</span></td>"
    print "</tr>"

    child_min.append(ancient_a[-1])
    child_max.append(ancient_a[-2])

    print "<tr>"
    print "<td>child_min sum: </td><td><span contenteditable=\"false\">" + str(reduce(lambda x,y:x+y, child_min)) + "</span></td>"
    print "</tr>"
    print "<tr>"
    print "<td>child_max sum: </td><td><span contenteditable=\"false\">" + str(reduce(lambda x,y:x+y, child_max)) + "</span></td>"
    print "</tr>"
#    print "---------------------------------------------------------+"
    print "</table>"

def reply():
    import cgi
    title = "Random Seq"
    
    print "Content-Type: text/html\n\n"
    print "<!DOCTYPE html>"
    print "<html>"
    
    print "<head>"
    print "<title>", title, "</title>"
    print "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    print "<meta charset=\"UTF-8\">"
    print "</head>"
    
    print "<body>"
    
    for i in [100, 10, 1000, 999, 3]:
        print "<h2>" + "Ranseq with " + str(i) + "</h2>"
        print ranseq(i)
    
    print "</body>"
    print "</html>"

reply()
