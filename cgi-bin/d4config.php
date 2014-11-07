<?php
/* d4config.php
 *
 * Author: Zex <top_zlynch@yahoo.com>
 */

include_once 'navi.php';

$CONFDB = "/home/ag/lab/Starter/dbs/config.db";
$SYSCONFTABLE = "SysConf";
$USERCONFTABLE = "UserConf";

function update_configure()
{
    global $CONFDB;
    global $SYSCONFTABLE;
    global $USERCONFTABLE;

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
                $item = ltrim(strrchr($k,'_'), '_');
                $key = rtrim(str_replace($item, "", $k), '_');
                $sql = "update ".$SYSCONFTABLE." set ".$item."=\"".$v."\" where Key == \"".str_replace('_', '.', $key)."\";";

                $conn->exec($sql);
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

function read_sysconf()
{
    global $CONFDB;
    global $SYSCONFTABLE;
    global $USERCONFTABLE;
   

    if (!($conn = new SQLite3($CONFDB)))
        echo $conn->lastErrorMsg();

    $titles = ["Key", "DefaultValue", "Step", "Upper", "Lower", "Unit"]; 

    $sql = "select ".join(",", $titles);
    $sql.rtrim(",");
    $sql .= " from ".$SYSCONFTABLE.";";
    
    if (!($ret = $conn->query($sql)))
    {
        echo $conn->lastErrorMsg();
    }
    else
    {
        echo "<form action=\"d4config.php\" method=\"post\" enctype=\"multipart/form-data\">";
        echo "<table class=\"normal\">";

        echo "<tr class=\"normal\">";
        foreach ($titles as $t)
            echo "<th class=\"normal\">".$t."</th>";
        echo "</tr>";

        while ($row = $ret->fetchArray(SQLITE3_ASSOC))
        {
            echo "<tr class=\"normal\">";
            echo "<td class=\"normal\">"."<span>".$row['Key']."</span>"."</td>";

            foreach ($titles as $t)
            {
                if ($t == 'Key') continue;

                echo "<td class=\"normal\">";
                echo "<input name=\"".$row['Key'].".".$t."\" type=\"text\" value=\"".$row[$t]."\"/>";
                echo "</td>";
            }

            echo "</tr>";
        }

        echo "</table>";
        echo "<input type=\"submit\" value=\""."Submit"."\"/>";
        echo "</form>";

    }

    $conn->close();
}

function read_userconf()
{
    global $CONFDB;
    global $SYSCONFTABLE;
    global $USERCONFTABLE;
   

    if (!($conn = new SQLite3($CONFDB)))
        echo $conn->lastErrorMsg();

    $titles = ["Key", "Value"];

    $sql = "select ".join(",", $titles);
    $sql.rtrim(",");
    $sql .= " from ".$USERCONFTABLE.";";

    if (!($ret = $conn->query($sql)))
    {
        echo $conn->lastErrorMsg();
    }
    else
    {
        echo "<table class=\"normal\">";

        echo "<tr class=\"normal\">";
        foreach ($titles as $t)
            echo "<th class=\"normal\">".$t."</th>";
        echo "</tr>";

        while ($row = $ret->fetchArray(SQLITE3_ASSOC))
        {
            echo "<tr class=\"normal\">";
            echo "<td class=\"normal\">"."<span>".$row['Key']."</span>"."</td>";

            foreach ($titles as $t)
            {
                if ($t == 'Key') continue;

                echo "<td class=\"normal\">";
                echo "<input name=\"".$row['Key'].'.'.$t."\" type=\"text\" value=\"".$row[$t]."\"/>";
                echo "</td>";
            }

            echo "</tr>";
        }

        echo "</table>";

    }
    
    $conn->close();
}

function reply()
{

    header("Content-type: text/html; charset=utf-8");
    
    echo "<!DOCTYPE html>";
    echo "<html>";
    
    default_head("4D Config");
    
    echo "<body>";
    default_navigator();
    echo "<div class=\"content\">";

    if (!empty($_POST))
        update_configure();

    echo "<h1>"."Configure for 3D/4D"."</h1>";

    echo "<h2>"."System Configure"."</h2>";
    read_sysconf();

    echo "<h2>"."User Configure"."</h2>";
    read_userconf();

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
