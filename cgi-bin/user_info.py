#!/usr/bin/env python
#
# user_info.py
# Author: Zex <top_zlynch@yahoo.com>

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
    print "<label>helo</label>"
    from pandas import DataFrame
    print "<label>helo</label>"
    xls = DataFrame(data)
    #xls.to_excel(xlsname, sheetname, index=False)
    return xls.to_html(index=False)

def reply():
    import cgi
#    fields = cgi.FieldStorage()
    title = "User Info"
    
    print "Content-Type: text/html\n\n"
    print "<!DOCTYPE html>"
    print "<html>"
    
    print "<head>"
    print "<title>", title, "</title>"
    print "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    print "<meta charset=\"UTF-8\">"
    print "</head>"
    
    print "<body>"
    
    print create_html('all-log-pandas.xls', 'user-info')
    
    print "</body>"
    print "</html>"

#if __name__ == '__main__':
reply()

