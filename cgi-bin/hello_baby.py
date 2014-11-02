#!/usr/bin/python

import cgi
from navi import *

fields = cgi.FieldStorage()
title = "Hello Baby"

print "Content-Type: text/html\n\n"
print "<!DOCTYPE html>"
print "<html>"

print "<head>"
print "<title>", title, "</title>"
print "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
print "<meta charset=\"UTF-8\">"
print "</head>"

print "<body>"

for k in fields.keys():
	print k, fields[k].value

print "</body>"
print "</html>"

