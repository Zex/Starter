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
from navi import *

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

    ret = "Content-Type: text/html\n\n"
    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += default_head("Where You Live") 
    ret += default_navigator() 

    ret += "<body>"
    ret += "<div class=\"content\">"

    try:

        if kwargs.has_key('addr'):
            whereyoulive(kwargs['addr'].value)
        elif kwargs.has_key('elseaddr'):
            whereyoulive(kwargs['elseaddr'].value)
        else:
            ret += "<span>No address selected. <span>Previous Result</span><br>"
    
        ret += whereyoulive_sum()

    except Exception as e:

        ret += "<div>" + e.message + "</div>"


    ret += "</div>"
    ret += "</body>"
    ret += "</html>"

    return ret

preset(sample)

if __name__ == '__main__':

    print reply({})
