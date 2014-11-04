#!/usr/bin/python

import cgi
from navi import *

fields = cgi.FieldStorage()
title = "Connect SVN"

# test setup
svn_addr_prefix = "svn://"
svn_addr = "192.168.0.104"
svn_top_path = svn_addr_prefix + svn_addr + '/11002/code/LinuxC/'
#svn_opt = ['--username', 'liyun', '--password', 'ag111111', '--no-auth-cache', '--non-interactive']

def svn_cat(cur_path, usern, passw):

    ret = ""
    svn_opt = ['--username', usern, '--password', passw, '--no-auth-cache', '--non-interactive']

    try:

        from subprocess import check_output
        from re import match

        if match('.*\.(jpg|png|bmp|jpeg)$', cur_path) != None:

            from os.path import basename

            buf = check_output(['svn', 'cat', cur_path] + svn_opt)

            with file('/tmp/'+basename(cur_path), 'w') as fd:
                fd.write(buf)

            from PIL import Image

            img = Image.open('/tmp/'+basename(cur_path))

            ret += "<div "# class=\"source\" "
            ret += "width=\"" + str(img.size[0]) + "\" height=\"" + str(img.size[1]) + "\">"
            #ret += "width=\"" + "100%" + "\" height=\"" + "100%" + "\"/>"
            
            ret += "<img src=\"/tmp/" + basename(cur_path) + "\" alt=\"" + basename(cur_path) + "\" "
            ret += "width=\"" + "100%" + "\" height=\"" + "100%" + "\"/>"
            ret += "</div>"

        else:

            buf = check_output(['svn', 'cat', cur_path] + svn_opt)
    
            ret += "<div class=\"normal\">"
            ret += "<textarea class=\"source\" readonly rows=\"" + str(buf.count('\n')) + "\">"
            ret += buf
            ret += "</textarea></div>"

    except Exception as e:

        ret += "<div>" + e.message + "</div>"

    return ret


def svn_list(cur_path, usern, passw):

    ret = ""
    svn_opt = ['--username', usern, '--password', passw, '--no-auth-cache', '--non-interactive']

    try:

        from subprocess import check_output

        for f in check_output(['svn', 'ls', cur_path] + svn_opt).split('\n'):

            if len(f) == 0: continue

            if f[-1] != '/':

                ret += "<div>"
                ret += "<a href=\"conn_svn.py?op=cat&path="
                
                ret += cur_path.replace(svn_top_path, '')
    
                ret += f + "\">" + f + "</a>"
                ret += "</div>"

            else:

                ret += "<div>"
                ret += "<a href=\"conn_svn.py?op=list&path="
                
                ret += cur_path.replace(svn_top_path, '')
    
                ret += f + "\">" + f + "</a>"
                ret += "</div>"

    except Exception as e:

        ret += "<div>" + e.message + "</div>"

    return ret

def svn_login(usern=None, passw=None):

    ret = ""

    try:

        if usern != None and passw != None:
    
            ret += svn_list(svn_top_path, usern, passw)
    
        else:
    
            ret += "<form action=\"conn_svn.py?op=login\" method=\"post\">"
            ret += "<table class=\"login\">"
        
            ret += "<tr class=\"login\">"
            ret += "<th class=\"login\">" + "Connecting to SVN"
            ret += "</th>"
            ret += "</tr>"
            ret += "<tr class=\"login\">"
            ret += "<td class=\"login\">"
            ret += "<label for=\"usern\">" + "Username" + "</label>"
            ret += "</td>"
            ret += "<td class=\"login\">"
            ret += "<input type=\"text\" name=\"usern\"/>"
            ret += "</td>"
            ret += "</tr>"
        
            ret += "<tr class=\"login\">"
            ret += "<td class=\"login\">"
            ret += "<label for=\"passw\">" + "Password" + "</label>"
            ret += "</td>"
            ret += "<td class=\"login\">"
            ret += "<input type=\"password\" name=\"passw\"/>"
            ret += "</td>"
            ret += "</tr>"
        
            ret += "<tr class=\"login\">"
            ret += "<td class=\"login\">"
            ret += "<input type=\"submit\" value=\"" + "Login" + "\"/>"
            ret += "</td>"
            ret += "</tr>"

            ret += "</table>"
            ret += "</form>"

    except Exception as e:

        ret += "<div class=\"normal\">" + e.message + "</div>"

    return ret

def reply():

    ret = ""

    ret += "Content-Type: text/html\n\n"
    ret += "<!DOCTYPE html>"
    ret += "<html>"

    ret += default_head(title)
    ret += default_navigator()

    ret += "<body>"
    ret += "<div class=\"content\">"

    svn_cur_path = ""

    try:
 
        if not fields.has_key('op'):

            ret += svn_login()
 
        else:

            if fields.has_key('usern') and fields.has_key('passw'):
        
                if fields['op'].value == 'login':
        
                    cookie = "Set-Cookie: usern=" + fields['usern'].value + '\n'
                    cookie += "Set-Cookie: passw=" + fields['passw'].value + ";Expires=" + str(24*60*60) + '\n'
        
                    ret = cookie + ret
                    ret += svn_login(fields['usern'].value, fields['passw'].value)
        
                else:
        
                    if fields.has_key('path'):
                        svn_cur_path = svn_top_path + fields['path'].value
                    else:
                        svn_cur_path = svn_top_path
                
                    ret += "<div><span>" + svn_cur_path.replace(svn_top_path, 'Location: /') + "</span></div><br>"
                    
                    if fields['op'].value == 'cat':
                        ret += svn_cat(svn_cur_path, fields['usern'].value, fields['passw'].value)
                    else:
                        ret += svn_list(svn_cur_path, fields['usern'].value, fields['passw'].value)
        
            else:
        
                from cgi import os
        
                if os.environ.has_key('HTTP_COOKIE'):
        
                    buf = os.environ['HTTP_COOKIE']
                    cookie ={ e.split('=')[0].strip():e.split('=')[1].strip() for e in buf.split(';') }
        
                    if cookie.has_key('usern') and cookie.has_key('passw'):
        
                        if fields.has_key('path'):
                            svn_cur_path = svn_top_path + fields['path'].value
                        else:
                            svn_cur_path = svn_top_path
                    
                        ret += "<div><span>" + svn_cur_path.replace(svn_top_path, 'Location: /') + "</span></div><br>"
       
                        if fields['op'].value == 'cat':
                            ret += svn_cat(svn_cur_path, cookie['usern'], cookie['passw'])
                        else:
                            ret += svn_list(svn_cur_path, cookie['usern'], cookie['passw'])
        
                    else:
        
                        ret += svn_login()


    except Exception as e:
        ret += "<div>" + e.message + "</div>"

    ret += "</div>"
    ret += "</body>"
    ret += "</html>"

    print ret

#ops = {
#    'login':svn_login,
#    'list':svn_list,
#    'cat':svn_cat,
#}

reply()
