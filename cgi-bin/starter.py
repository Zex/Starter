#!/usr/bin/env python
#
# Starter.py
# Author: Zex <top_zlynch@yahoo.com>
#

from navi import *

def starter():

    import time
    
    ret = "Content-Type: text/html\n\n"
    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += default_head("Starter")
    ret += default_navigator()

    ret += "<body>"
    ret += "<div class=\"content\">"
    ret += "<div class=\"normal\">"
    ret += "<img src=\"/img/cattail.jpg\" height=200px>"
    ret += "</div>"

    ret += "<div class=\"normal\">"
    ret += "<a name=\"YouOut\"></a>"
    ret += "<a href=\"#Navigator\" title=\"Navigator\">Navigator</a>"
    ret += "<form name=\"Youout\" action=\"youout.py\" method=\"get\">"
    ret += "<label for=\"total_player\"><b>Total player: </b></label>"
    ret += "<input type=\"text\" name=\"total_player\"/><br>"
    ret += "<label for=\"total_player\"><b>The unlucky one: </b></label>"
    ret += "<input type=\"text\" name=\"unlucky_n\"/><br>"
    ret += "<input type=\"submit\" value=\"You Out :D\"/>"
    ret += "</form>"
    ret += "</div>"
    
    ret += "<div class=\"normal\">"
    ret += "<a href=\"#Navigator\" title=\"Navigator\">Navigator</a>"
    ret += "<form action=\"upload_file.py\" method=\"post\" enctype=\"multipart/form-data\">"
    ret += "<label><b>Select file: </b></label>"
    ret += "<input type=\"file\" name=\"file_name\"/>"
    ret += "<input type=\"submit\" value=\"Upload!\"/><br>"
    ret += "</form>"
    ret += "</div>"
    
    ret += "<table class=\"normal\">"
    
    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">"
    icecreams = [ "Milk", "Chocolate", "Strawberry", "Coconut", "Peanut" ]
    
    ret += "<form action=\"icecream_box.py\" method=\"post\">"
    ret += "<label><b>Icecream: </b></label><br>"
    
    for i in icecreams:
        ret += "<input type=checkbox name=\"" + str(i) + "\" value=\"1\"/> <b>" + str(i) + "</b><br>"
    
    ret += "<input type=\"submit\" value=\"Done!\"/><br>"
    ret += "</form>"
    ret += "</td>"
    ret += "<td class=\"normal\">"
    
    flowers = [ "Almond Blossom", "Balsam", "Anther", "Camellia", "Azalea" ]
    
    ret += "<form action=\"flower_man.py\" method=\"post\">"
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
    ret += "<a name=\"Motions\"></a>"
    ret += "<a href=\"#Navigator\" title=\"Navigator\">Navigator</a>"
    ret += "<form action=\"motion_trigger.py\" method=\"post\">"
    ret += "<label for=option><b>Motions</b></a>:</label><br>"
    ret += "<select name=option>"
    
    for o in options:
        ret += "<option>" + o
    
    ret += "</select>"
    ret += "<input type=\"submit\" value=\"Done!\"/><br>"
    ret += "</form>"
    ret += "</div>"
    
    ret += "<div class=\"normal\">"
    ret += "<a name=\"ConnSVN\"></a>"
    ret += "<form action=\"conn_svn.py\" method=\"post\">"
    ret += "<input type=\"submit\" name=\"ConnSVN\" value=\"Connect SVN\"/>"
    ret += "</form>"
    ret += "</div>"
#    ret += "<div class=\"normal\">"
#    ret += "<label><b>Current time: </b><label>"
#    ret += "<input id=\"cur_time\" type=\"text\" readonly=\"true\" value=\"" + time.strftime(time.asctime()) + "\"/><br>"
#    ret += "</form>"
#    ret += "</div>"
    
    ret += "<div class=\"normal\">"
    ret += "<a name=\"LeaveMessage\"></a>"
    ret += "<a href=\"#Navigator\" title=\"Navigator\">Navigator</a>"
    ret += "<form action=\"leave_message.py\" method=\"post\">"
    ret += "<label for=msgbox><b>Leave a Message: </b></label><br>"
    ret += "<textarea id=\"msgbox\" name=\"msgbox\"></textarea><br>"
    ret += "<input type=\"submit\" value=\"Submit\"/><br>"
    ret += "</form>"
    ret += "</div>"
   
    ret += "<div class=\"normal\"><a href=\"#Navigator\" title=\"Navigator\">Navigator</a></div>"

    ret += "<table class=\"normal\">"
    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">"
    ret += "<form action=\"user_info.py\" method=\"get\">"
    ret += "<input type=\"submit\" value=\"User Info\"/><br>"
    ret += "</form>"
    ret += "</td>"
    
    ret += "<td class=\"normal\">"
    ret += "<a name=\"RandomSeq\"></a>"
    ret += "<form action=\"ranseq.py\" method=\"get\">"
    ret += "<input type=\"submit\" value=\"Random Seq\"/><br>"
    ret += "</form>"
    ret += "</td>"
    
    ret += "<td class=\"normal\">"
    ret += "<form action=\"roman_number.py\" method=\"get\">"
    ret += "<span>Arabic/Roman Number </span><input name=\"rnum\" type=\"text\"/><br>"
    ret += "</form>"
    ret += "</td>"
    
    ret += "<td class=\"normal\">"
    ret += "<form action=\"plotting.py\" method=\"get\">"
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
