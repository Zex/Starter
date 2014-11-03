#!/usr/bin/python

import cgi
from navi import *

fields = cgi.FieldStorage()
title = "Connect SVN"

# test setup
svn_addr_prefix = "svn://"
svn_addr = "192.168.0.104"
svn_top_path = svn_addr_prefix + svn_addr + '/11002/code/LinuxC/'
svn_opt = ['--username', 'liyun', '--password', 'ag111111', '--no-auth-cache', '--non-interactive']

def svn_cat(cur_path):

    ret = ""

    try:

        from subprocess import check_output
        from re import match

        
        if match('.*[jpg|png|bmp|jpeg]$', cur_path) != None:

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


def svn_list(cur_path):

    ret = ""

    try:

        from subprocess import check_output

        for f in check_output(['svn', 'ls', cur_path] + svn_opt).split('\n'):

            if len(f) == 0: continue

            if f[-1] != '/':

                ret += "<div>"
                ret += "<a href=\"conn_svn.py?cat=1&path="
                
                ret += cur_path.replace(svn_top_path, '')
    
                ret += f + "\">" + f + "</a>"
                ret += "</div>"

            else:

                ret += "<div>"
                ret += "<a href=\"conn_svn.py?path="
                
                ret += cur_path.replace(svn_top_path, '')
    
                ret += f + "\">" + f + "</a>"
                ret += "</div>"

    except Exception as e:

        ret += "<div>" + e.message + "</div>"

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

#    for k in fields.keys():
#	    ret += "<div>" + k + " => " + fields[k].value + "</div>"
    svn_cur_path = ""
    
    if fields.has_key('path'):
        svn_cur_path = svn_top_path + fields['path'].value
    else:
        svn_cur_path = svn_top_path

    ret += "<div><span>" + svn_cur_path.replace(svn_top_path, 'Location: /') + "</span></div><br>"
    
    if fields.has_key('cat') and fields['cat'].value == '1':
        ret += svn_cat(svn_cur_path)
    else:
        ret += svn_list(svn_cur_path)

    ret += "</div>"
    ret += "</body>"
    ret += "</html>"

    print ret

reply()
