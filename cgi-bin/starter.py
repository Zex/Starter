#!/usr/bin/env python
#
# Starter.py
# Author: Zex <top_zlynch@yahoo.com>
#

def starter():

    import time
    
    ret = "Content-Type: text/html\n\n"
    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head>"
    ret += "<title>Starter</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<link href=\"/img/badsmile.jpg\" rel=\"icon\" type=\"image/jpg\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head><body>"

    ret += "<div class=\"navigator\">"
    ret += "<a name=\"Navigator\"><ul>Navigator</ul></a>"
    ret += "<ul>"
    ret += "<li><a href=\"#Motions\" title=\"Motions\">Motions</a></li>"
    ret += "<li><a href=\"#RandomSeq\" title=\"Random Seq\">Random Seq</a></li>"
    ret += "<li><a href=\"#LeaveMessage\" title=\"Leave a Message\">Leave a Message</a></li>"
    ret += "</ul>"
    ret += "</div>"

    ret += "<div class=\"content\">"
    ret += "<div class=\"normal\">"
    ret += "<img src=\"/img/cattail.jpg\" height=200px>"
    ret += "</div>"

    ret += "<div class=\"normal\">"
    ret += "<a href=\"#Navigator\" title=\"Navigator\">Navigator</a>"
    ret += "<form action=\"hello_baby.py\" method=get>"
    ret += "<label><b>Action: </b></label>"
    ret += "<input type=\"text\" name=\"fr_name\"/>"
    ret += "<input type=\"submit\" value=\"Do IT!\"/><br>"
    ret += "</form>"
    ret += "</div>"
    
    ret += "<div class=\"normal\">"
    ret += "<a href=\"#Navigator\" title=\"Navigator\">Navigator</a>"
    ret += "<form action=\"upload_file.py\" method=post enctype=\"multipart/form-data\">"
    ret += "<label><b>Select file: </b></label>"
    ret += "<input type=\"file\" name=\"file_name\"/>"
    ret += "<input type=\"submit\" value=\"Upload!\"/><br>"
    ret += "</form>"
    ret += "</div>"
    
    ret += "<table class=\"normal\">"
    
    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">"
    icecreams = [ "Milk", "Chocolate", "Strawberry", "Coconut", "Peanut" ]
    
    ret += "<form action=\"icecream_box.py\" method=post>"
    ret += "<label><b>Icecream: </b></label><br>"
    
    for i in icecreams:
        ret += "<input type=checkbox name=\"" + str(i) + "\" value=\"1\"/> <b>" + str(i) + "</b><br>"
    
    ret += "<input type=\"submit\" value=\"Done!\"/><br>"
    ret += "</form>"
    ret += "</td>"
    ret += "<td class=\"normal\">"
    
    flowers = [ "Almond Blossom", "Balsam", "Anther", "Camellia", "Azalea" ]
    
    ret += "<form action=\"flower_man.py\" method=post>"
    ret += "<label><b>Flower: </b></label><br>"
    
    for f in flowers:
        ret += "<input type=\"radio\" name=\"flower\" value=\"" + str(f) + "\"/> <b>" + str(f) + "</b><br>"
    
    ret += "<input type=\"submit\" value=\"Done!\"/><br>"
    ret += "</form>"
    ret += "</td>"
    ret += "</tr>"
    ret += "</table>"
    
    options = [ "Go", "Walk Away", "Close", "Laught" ]
    ret += "<div class=\"normal\">"
    ret += "<a href=\"#Navigator\" title=\"Navigator\">Navigator</a>"
    ret += "<form action=\"motion_trigger.py\" method=post>"
    ret += "<label for=option><a name=\"Motions\"><b>Motions</b></a>:</label><br>"
    ret += "<select name=option>"
    
    for o in options:
        ret += "<option>" + o
    
    ret += "</select>"
    ret += "<input type=\"submit\" value=\"Done!\"/><br>"
    ret += "</form>"
    ret += "</div>"
    
    ret += "<div class=\"normal\">"
    ret += "<label><b>Current time: </b><label>"
    ret += "<input id=\"cur_time\" type=\"text\" readonly=\"true\" value=\"" + time.strftime(time.asctime()) + "\"/><br>"
    ret += "</form>"
    ret += "</div>"
    
    ret += "<div class=\"normal\">"
    ret += "<a href=\"#Navigator\" title=\"Navigator\">Navigator</a>"
    ret += "<form action=\"leave_message.py\" method=post>"
    ret += "<a name=\"LeaveMessage\"><label for=msgbox><b>Leave a Message: </b></label></a><br>"
    ret += "<textarea id=\"msgbox\" name=\"msgbox\"></textarea><br>"
    ret += "<input type=\"submit\" value=\"Submit\"/><br>"
    ret += "</form>"
    ret += "</div>"
   
    ret += "<div class=\"normal\"><a href=\"#Navigator\" title=\"Navigator\">Navigator</a></div>"

    ret += "<table class=\"normal\">"
    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">"
    ret += "<form action=\"user_info.py\" method=get>"
    ret += "<input type=\"submit\" value=\"User Info\"/><br>"
    ret += "</form>"
    ret += "</td>"
    
    ret += "<td class=\"normal\">"
    ret += "<form action=\"ranseq.py\" method=get>"
    ret += "<a name=\"RandomSeq\"><input type=\"submit\" value=\"Random Seq\"/></a><br>"
    ret += "</form>"
    ret += "</td>"
    
    ret += "<td class=\"normal\">"
    ret += "<form action=\"roman_number.py\" method=get>"
    ret += "<span>Arabic/Roman Number </span><input name=\"rnum\" type=\"text\"/><br>"
    ret += "</form>"
    ret += "</td>"
    
    ret += "<td class=\"normal\">"
    ret += "<form action=\"plotting.py\" method=post>"
    ret += "<input type=\"submit\" value=\"Plot\"/><br>"
    ret += "</form>"
    ret += "</td>"
    
    ret += "<td class=\"normal\">"
    ret += "<form action=\"whereyoulive.py\" method=\"post\">"
    ret += "<input type=\"submit\" value=\"Where You Live\"/><br>"
    ret += "</form>"
    ret += "</td>"
    
    ret += "</tr>"
    ret += "</table>"
    
    ret += "</div>"

    ret += "</body>"
    ret += "</html>"

    print ret

if __name__ == '__main__':
    starter()
