#!/usr/bin/env python
#
# user_info.py
# Author: Zex <top_zlynch@yahoo.com>

from navi import *

def create_html(xlsname, sheetname):

    data = {}
    data['userid'] = [23,4,36,14,1,63,123]
    data['useremail'] = [
        'x3sd@sfsf.com',
        'x5sd@sfsf.com',
        'x2sd@sfsf.com',
        'x4sd@sfsf.com',
        'xasd@sfsf.com',
        'x35sd@sfsf.com',
        'x234sd@sfsf.com',
    ]

    from pandas import DataFrame
    xls = DataFrame(data)
    #xls.to_excel(xlsname, sheetname, index=False)
    return xls.to_html(index=False)

def reply():

    title = "User Info"
    ret = ""
    
    ret += "Content-Type: text/html\n\n"
    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += default_head(title) 
    ret += default_navigator() 

    ret += "<body>"
    
    ret += create_html('all-log-pandas.xls', 'user-info')
    
    ret += "</body>"
    ret += "</html>"

    print ret

#if __name__ == '__main__':

from os import environ

environ['MPLCONFIGDIR'] = "/tmp"

try:
    reply()
except Exception as e:
    print e
