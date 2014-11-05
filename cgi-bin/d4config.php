<?php
/* d4config.php
 *
 * Author: Zex <top_zlynch@yahoo.com>
 */

include_once 'sqlite3';
include_once 'navi.php';

$CONFDB = "/home/ag/lab/Starter/dbs/UserConf.db";
$CONFTABLE = "UserConf";

function update_configure()
{
    global $CONFDB;
    global $CONFTABLE;

    if (!($conn = new SQLite3($CONFDB)))
    {
        echo $conn->lastErrorMsg();
    }
    else
    {
        try
        {
            foreach ($_POST as $k => $v)
            {
                $sql = "update ".$CONFTABLE." set Value=\"".$v."\" where Key == \"".str_replace('_', '.', $k)."\";";
            }

            echo "<div><span>"."Configure updated !"."</span></div>";
        }
        catch (Exception $e)
        {
            echo "<div>".$conn->lastErrorMsg()."</div>";
        }
    }
    
    $conn->close();
}

function default_reply()
{
    global $CONFDB;
    global $CONFTABLE;

   
    if (!($conn = new SQLite3($CONFDB)))
        echo $conn->lastErrorMsg();
 
    $sql = "select Key, Value from ".$CONFTABLE.";";
    
    if (!($ret = $conn->query($sql)))
    {
        echo $conn->lastErrorMsg();
    }
    else
    {
        echo "<h2>"."Configure for 3D/4D"."</h2>";

        echo "<form action=\"d4config.php\" method=\"post\" enctype=\"multipart/form-data\">";
        echo "<table width=\"60%\" align=\"center\">";

        while ($row = $ret->fetchArray(SQLITE3_ASSOC))
        {
            echo "<tr class=\"normal\">";

            echo "<td class=\"normal\">";
            echo "<span>".$row['Key']."</span>";
            echo "</td>";

            echo "<td class=\"normal\">";
            echo "<input name=\"".$row['Key']."\" width=\"100%\" type=\"text\" value=\"".$row['Value']."\"/>";
            echo "</td>";

            echo "</tr>";
        }

        echo "<tr>";
        echo "<td>";
        echo "<input type=\"submit\" value=\""."Submit"."\"/>";
        echo "<td>";
        echo "</tr>";
        echo "</table>";
        echo "</form>";
    }
    
    $conn->close();
}

function reply()
{

    header("Content-type: text/html; charset=utf-8");
    
    echo "<!DOCTYPE html>";
    echo "<html>";
    
    default_head("4D Config");
    default_navigator();
    
    echo "<body>";
    echo "<div class=\"content\">";

    if (!empty($_POST))
        update_configure($conn);

    default_reply();

    echo "</div>";
    echo "</body>";
    echo "</html>";
}

try
{
    reply();
}
catch (Exception $e)
{
    die ('d4config Error: ' . $e->getMessage());
}

?>
