
<?php
/* index.php
 *
 * Author: Zex <top_zlynch@yahoo.com>
 */

if ($_SERVER['REMOTE_ADDR'] == '192.168.0.205')
{
    echo "<html>";
    echo "<title>Starter</title>";
    echo "<body>";
    echo "<h1>Starter</h1>";
    echo "<meta http-equiv=Refresh Content="0; Url=cgi-bin/starter.py">";
    echo "</body>";
    echo "</html>";
}
else
{
    echo "<html>";
    echo "<title>Starter</title>";
    echo "<body>";
    echo "<img src=\"/img/molecular-random-motion-xxx.png\">"
    echo "</body>";
    echo "</html>";
}

?>
