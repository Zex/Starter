<?php
/* srcview.php
 *
 * Author: Zex <top_zlynch@yahoo.com>
 */

require_once 'Zend/Loader/Autoloader.php';
$loader = Zend_Loader_Autoloader::getInstance();
$date_fmt =  "D M Y H:m:s";
$now = date($date_fmt);

function get_all_groups($curdir, $groups)
{
    $dirfd = dir($curdir);

    while (false !== ($entry = $dirfd->read())) {

        if (ereg("^\.", $entry))
            continue;

        if (is_dir($curdir."/".$entry))
            $groups += get_all_groups($curdir."/".$entry, $groups);
        else 
            array_push($groups, $curdir."/".$entry);
    }

    return $groups;
}

function clean_path_all($path) {
    foreach(glob($path."/*") as $x) {
        if (is_dir($x)) {
            clean_path_all($x);
//            rmdir($x);
        }
        else
            unlink($x);
    }

    rmdir($path);
}

if (empty($_FILES)) {

    header("Content-type: text/html; charset=utf-8");

    echo "<!DOCTYPE html>";
    echo "<html>";
    echo "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">";
    echo "<link href=\"/img/badsmile.jpg\" rel=\"icon\" type=\"image/jpg\">";
    echo "<body>";

    echo "<div class=\"navigator\">";
    echo "<a name=\"Navigator\"><ul>Navigator</ul></a>";
    echo "<ul>";
    echo "<li><a href=\"index#Motions\" title=\"Motions\">Motions</a></li>";
    echo "<li><a href=\"index#RandomSeq\" title=\"Random Seq\">Random Seq</a></li>";
    echo "<li><a href=\"index#LeaveMessage\" title=\"Leave a Message\">Leave a Message</a></li>";
    echo "</ul>";
    echo "</div>";

    echo "<div class=\"content\">";

    echo "<h2>Welcome, ".getenv("REMOTE_ADDR")."!</h2>";
    echo "<span>".getenv("HTTP_USER_AGENT")."</span><br><br>";

    echo "<div class=\"normal\">";
    echo "<a href=\"#Navigator\" title=\"Navigator\">Navigator</a>";
    echo "<form action=\"srcview.php\" method=\"post\" enctype=\"multipart/form-data\">";
    echo "<label><b>Source package: </b></label>";
    echo "<input type=\"file\" name=\"srcpkg\"/><br>";
    echo "<label>Project name: </label><input type=\"text\" name=\"proj\"/><br>";
    echo "<label>Project version: </label><input type=\"text\" name=\"proj_ver\"/><br>";
    echo "<input type=\"submit\" value=\"Upload!\"/><br>";
    echo "</form>";
    echo "</div>";

    echo "<br><br><div>".$now."</div>";

    echo "</div>";
    echo "</body>";
    echo "</html>";

} else { try {

    $tmp_remote_dir = "/tmp/".getenv("REMOTE_ADDR").str_replace(" ", "-", $now);
    $pkg_path = "/tmp/".$_FILES["srcpkg"]["name"];

    mkdir($tmp_remote_dir);

    system("tar xf ".$_FILES["srcpkg"]["tmp_name"]." -C".$tmp_remote_dir);

    $pdf = new Zend_Pdf();
    $font = Zend_Pdf_Font::fontWithName(Zend_Pdf_Font::FONT_HELVETICA);
    $font_sz = 10;
    $line_space = 1;
    $indent = 15;
    $page_space = $font_sz*4;

    $respath = "/tmp";
    $proj = $_POST["proj"];//"EasySipTs";
    $projver = $_POST["proj_ver"];// "v123.44.567";

    if (0 == strlen($proj))
        $proj = preg_split("/[\s\.]+/", basename($pkg_path))[0];

    if (0 == strlen($projver))
        $projver = "v0.0.0";

    $outfile = $proj."-".$projver;
    $dirpath = $tmp_remote_dir;//"../../EasySipTs";
    $groups = get_all_groups($dirpath, []);
    $srcs = [];


    foreach ($groups as $f) {
        if (ereg(".*\.[cpp|c|h]", $f)) {
            array_push($srcs, $f);
        }
    }

    $page_nr = 0;

    /* generate each file */
    foreach ($srcs as $filename) {

        $buf = file($filename);

        $page = new Zend_Pdf_Page(Zend_Pdf_Page::SIZE_A4);
        $page->setFont($font, $font_sz);
        $limit_width = $page->getWidth()-$indent*2;
        $line_nr = $page_space;
        $page_nr ++;
        $pg_head = $now."  ".$outfile."-".$filename;
    
        /* generate project name */
        $page->drawText($pg_head, ($limit_width-strlen($pg_head))/4, $page->getHeight()-20);
        $page->drawText($page_nr, $limit_width, $page->getHeight()-20);
        $line_nr += ($font_sz + $line_space)*2;

//        /* generate file name */
//        $page->drawText($filename, $indent/2, $page->getHeight()-$line_nr);
//        $line_nr += $font_sz + $line_space*2;

        /* generate each page */
        foreach ($buf as $nr => $line) {

            $ind = 0;

            /* generate each line */
            while ($ind < strlen($line)) {

                $page->drawText(substr($line, $ind, $limit_width), $indent, $page->getHeight()-$line_nr);
                $line_nr += $font_sz + $line_space;
                $ind += $limit_width;

                if ($line_nr > $page->getHeight()-$page_space) {
    
                    $pdf->pages[$page_nr] = $page;
    
                    $page = new Zend_Pdf_Page(Zend_Pdf_Page::SIZE_A4);
                    $page->setFont($font, $font_sz);
                    $line_nr = $page_space;
                    $page_nr ++;
                
                    /* generate project name */
                    $page->drawText($pg_head, ($limit_width-strlen($pg_head))/4, $page->getHeight()-20);
                    $page->drawText($page_nr, $limit_width, $page->getHeight()-20);
                    $line_nr += ($font_sz + $line_space)*2;
                }
            }
        }
    
        if ($line_nr > $page_space) {
            $pdf->pages[$page_nr] = $page;
        }
    }
    
    $pdf->save($respath."/".$outfile.".pdf");

    header("Content-type: text/html; charset=utf-8");

    echo "<!DOCTYPE html>";
    echo "<html>";
    echo "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">";
    echo "<link href=\"/img/badsmile.jpg\" rel=\"icon\" type=\"image/jpg\">";
    echo "<body>";

    echo "<div class=\"navigator\">";
    echo "<a name=\"Navigator\"><ul>Navigator</ul></a>";
    echo "<ul>";
    echo "<li><a href=\"index#Motions\" title=\"Motions\">Motions</a></li>";
    echo "<li><a href=\"index#RandomSeq\" title=\"Random Seq\">Random Seq</a></li>";
    echo "<li><a href=\"index#LeaveMessage\" title=\"Leave a Message\">Leave a Message</a></li>";
    echo "</ul>";
    echo "</div>";

    echo "<div class=\"content\">";

    echo "<h2>Welcome, ".getenv("REMOTE_ADDR")."!</h2>";
    echo "<span>".getenv("HTTP_USER_AGENT")."</span><br><br>";

    echo "<div>Source package: ".$_FILES["srcpkg"]["name"]."</div>";
    echo "<div>SrcView: "."<a href=".$respath."/".$outfile.".pdf".">"."<span>".$outfile.".pdf"."</span>"."</a>"." generated!</div>";
    echo "<div>Total page: ".($page_nr+1)."</div>";
    echo "<br><br><div>".$now."</div>";

    echo "</div>";
    echo "</body>";
    echo "</html>";

//    header("Content-type: application/pdf");
//    header("Content-Disposition: attachment;Filename=".$outfile.".pdf");

    clean_path_all($tmp_remote_dir);

    } catch (Exception $e) {
       die ('Application error: ' . $e->getMessage());
    }
}

?>
