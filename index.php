<?php
/* index.php
 *
 * Author: Zex <top_zlynch@yahoo.com>
 */

include_once 'cgi-bin/navi.php';

header("Content-type: text/html; charset=utf-8");
    
echo "<!DOCTYPE html>";

if ($_SERVER['REMOTE_ADDR'] == '192.168.0.205')
{
    echo "<html>";
    default_head("Starter");
    echo "<body>";
    echo "<div class=\"content\">";
    echo "<h1>Starter</h1>";
    echo "<meta http-equiv=Refresh Content=\"0; Url=cgi-bin/starter.py\">";
    echo "</div>";
    echo "</body>";
    echo "</html>";
}
else
{
    echo "<html>";
    default_head("Starter");
    echo "<body>";
    echo "<div class=\"content\">";
    echo "<img src=\"/img/molecular-random-motion-xxx.png\">";
    echo "</div>";
    echo "</body>";
    echo "</html>";
}

?>
