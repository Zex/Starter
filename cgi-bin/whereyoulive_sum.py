#!/usr/bin/env python
#
# cgi-bin/whereyoulive_sum.py
# Survay of where my colleagues live
#
# Author: zex <top_zlynch@yahoo.com>
#
# http://localhost:8080/whereyoulive

from memcache import Client
from socket import gethostname, gethostbyname

# addr -> count

addr_prefix = 'staff.address.'
sample = "../res/Addrs.Sample"

with open(sample, 'r') as fd:
   addresses = [ p.replace('\n', '') for p in fd.readlines() ]

def preset(sample):

    global addresses
    conn = Client([gethostname()+':11211'])

    if conn.get_stats()[0][1]['curr_items'] == 0:

        for k in addresses:
            conn.set(addr_prefix+k, 0)

def whereyoulive(addr):

    conn = Client([gethostname()+':11211'])

    if conn.get(addr_prefix+addr) != None:
        conn.incr(addr_prefix+addr)

    else:
        conn.set(addr_prefix+addr, 1)

    if not addresses.__contains__(addr):
        addresses.append(addr)
        
def whereyoulive_sum():

    global addresses
    
    ret = "<table class=\"normal\">"
    ret += "<th class=\"normal\">" + "Address" + "</th>"
    ret += "<th class=\"normal\">" + "Total/Address" + "</th>"

    conn = Client([gethostname()+':11211'])

    vals = []
    
    for k in addresses:
        ret += "<tr class=\"normal\">"
        ret += "<td class=\"normal\">" + k + "</td>"
        val = conn.get(addr_prefix+k)

        if val == None:
            vals.append(0)
        else:
            vals.append(val)

        ret += "<td class=\"normal\"><span>" + str(vals[-1]) + "</span></td>"
        ret += "</tr>"

    ret += "<tr align=\"center\"><td class=\"normal\">" + "Sum" + "</td>"

    if len(vals) == 0:
        ret += "<td class=\"normal\">" + "0" + "</td></tr>"
    else:
        ret += "<td class=\"normal\">" + str(reduce(lambda i, j : i+j, [i for i in vals])) + "</td></tr>"

    ret += "</table>"

    return ret

def reply(kwargs):

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

    if kwargs.has_key('addr'):
        whereyoulive(kwargs['addr'].value)
    elif kwargs.has_key('elseaddr'):
        whereyoulive(kwargs['elseaddr'].value)
    else:
        ret += "<span>No address selected. <span>Previous Result</span><br>"

    ret += whereyoulive_sum()

    ret += "</div>"
    ret += "</body>"
    ret += "</html>"

    return ret

preset(sample)
