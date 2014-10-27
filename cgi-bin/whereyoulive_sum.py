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

def preset(sample):

    ret = {}
    conn = Client([gethostname()+':11211'])

#    if conn.get_stats()[0][1]['curr_items'] == 0:
    if 1: # load address info from sample addresses
        with open(sample, 'r') as fd:
            addresses = { p.split('\n')[0]:0 for p in fd.readlines() }

        for k, v in addresses.items():
            print "++++++++++", k, v
            conn.set(addr_prefix+k, v)
            ret[k] = v

#    else:
#        for k, v in conn.get_multi(keys, key_prefix=addr_prefix).items():
#            ret[k] = v

    return ret

def whereyoulive(addr):

    conn = Client([gethostname()+':11211'])

    if conn.get(addr_prefix+addr) != None:
        conn.incr(addr_prefix+addr)

    else:
        conn.set(addr, 1)
        
def whereyoulive_sum():

    ret = "<table class=\"normal\">"
    ret += "<th class=\"normal\">" + "Address" + "</th>"
    ret += "<th class=\"normal\">" + "Total/Address" + "</th>"

    conn = Client([gethostname()+':11211'])
#    vals = []
#
#    for x in conn.zrange(addr_prefix, 0, conn.zcard(addr_prefix)):
#        ret += "<tr class=\"normal\">"
#        ret += "<td class=\"normal\">" + x + "</td>"
#        vals.append(int(conn.zscore(addr_prefix, x)))
#        ret += "<td class=\"normal\"><span>" + str(vals[-1]) + "</span></td>"
#        ret += "</tr>"
#
#    ret += "<tr align=\"center\"><td class=\"normal\">" + "Sum" + "</td>"
#    if len(vals) == 0:
#        ret += "<td class=\"normal\">" + "0" + "</td></tr>"
#    else:
#        ret += "<td class=\"normal\">" + str(reduce(lambda i, j : i+j, [i for i in vals])) + "</td></tr>"
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

    ret += "<div id=\"content\">"

    if kwargs.has_key('addr'):
        whereyoulive(kwargs['addr'])
    elif kwargs.has_key('elseaddr'):
        whereyoulive(kwargs['elseaddr'])
    else:
        ret += "<span>No address selected. <span>Previous Result</span><br>"

    ret += whereyoulive_sum()

    ret += "</div>"
    ret += "</body>"
    ret += "</html>"

    print ret

#preset("../res/Addrs.Sample")
