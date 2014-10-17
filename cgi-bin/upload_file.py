#!/usr/bin/env python

def reply():

    import cgi
    
    fields = cgi.FieldStorage()
    title = fields["file_name"].value
    
    print "Content-Type: text/html\n\n"
    print "<!DOCTYPE html>"
    print "<html>"
    
    print "<head>"
    print "<title>", title,"</title>"
    print "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    print "<meta charset=\"UTF-8\">"
    print "</head>"
    
    print "<body>"

    #while line = fields["file_name"].file.read():
	#    print "<p><b>", line,"</b></p>"

    for k in fields["file_name"].file.readlines():

    	print "<b>" + "File Name: " + fields["file_name"].value + "</b><br>"
        print "<span contenteditable=\"false\">"

        with open("../uploads/" + fields["file_name"].value, 'w') as fd:

            for line in k[1].file.readlines():
             	print  line + "<br>"
                fd.write(line)

        print "</span>"


    print "</body>"
    print "</html>"

reply()
