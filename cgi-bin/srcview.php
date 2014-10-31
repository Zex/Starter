<?php
/* srcview.php
 *
 * Author: Zex <top_zlynch@yahoo.com>
 */

require_once 'Zend/Loader/Autoloader.php';
include_once 'navi.php';

$loader = Zend_Loader_Autoloader::getInstance();
$date_fmt =  "j M Y H:m:s";
date_default_timezone_set('UTC');
$now = date($date_fmt);

function get_path_groups($path)
{
    $groups = [];

    foreach (scandir($path) as $entry) {

        if (ereg("^\.", $entry)) 
            continue; 

        $entry = $path."/".$entry;

        if (is_dir($entry)) {
            $groups += get_path_groups($entry);
        }
        else {
            array_push($groups, $entry);
        }
    }

    return $groups;
}

function clean_path_all($path)
{
    foreach (scandir($path) as $entry) {

        if (ereg("^\.{1,2}$", $entry)) 
            continue; 

        $rm_entry = $path."/".$entry;

        if (is_dir($rm_entry)) {
            clean_path_all($rm_entry);
        }
        else {
            unlink($rm_entry);
        }
    }

    rmdir($path);
}

function get_src_groups($path, &$groups)
{
    foreach (scandir($path) as $entry) {

//      if (ereg("^[^(\.)].*$", $entry)) {
        if (ereg("^\.", $entry)) 
            continue; 

        $entry = $path."/".$entry;

        if (is_dir($entry)) {
            get_src_groups($entry, $groups);
        }
        else {
            if (ereg("^.*\.(cpp|h|cxx|hpp)$", $entry))
                array_push($groups, $entry);
        }
    }
}

function reply_default() {

    header("Content-type: text/html; charset=utf-8");

    echo "<!DOCTYPE html>";
    echo "<html>";

    echo "<body>";

    default_head("SrcView");
    default_navigator();

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
    echo "<label>Page limit(default: no limitation): </label><input type=\"text\" name=\"page_nr_max\"/><br>";
    echo "<input type=\"submit\" value=\"Upload!\"/><br>";
    echo "</form>";
    echo "</div>";

    global $now;
    echo "<br><br><div>".$now."</div>";

    echo "</div>";
    echo "</body>";
    echo "</html>";
}

if (empty($_FILES)) {

    reply_default();

} else { try {

    $tmp_remote_dir = "/tmp/".getenv("REMOTE_ADDR").'-'.str_replace(" ", "-", $now);
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
    $page_nr_max = intval($_POST["page_nr_max"]);

    if (0 == strlen($proj))
        $proj = preg_split("/[\s\.]+/", basename($pkg_path))[0];

    if (0 == strlen($projver))
        $projver = "v0.0.0";

    $outfile = $proj."-".$projver;
    $dirpath = $tmp_remote_dir;
    $srcs = [];
    
    get_src_groups($dirpath, $srcs);

    /* generate each file */
    foreach ($srcs as $filename) {

        $buf = file($filename);

        $page = new Zend_Pdf_Page(Zend_Pdf_Page::SIZE_A4);
        $page->setFont($font, $font_sz);
        $limit_width = $page->getWidth()-$indent*2;
        $line_nr = $page_space;
        $pg_head = $now."  ".$outfile."-".str_replace($tmp_remote_dir, "", $filename);
    
        /* generate project name */
        $page->drawText($pg_head, ($limit_width-strlen($pg_head))/4, $page->getHeight()-20);
        $page->drawText(sizeof($pdf->pages)+1, $limit_width, $page->getHeight()-20);
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

                if ($page_nr_max > 0 && $page_nr_max < sizeof($pdf->pages)+1)
                    break;

                if ($line_nr > $page->getHeight()-$page_space) {
    
                    //$pdf->pages[$page_nr] = $page;
                    array_push($pdf->pages, $page);
    
                    $page = new Zend_Pdf_Page(Zend_Pdf_Page::SIZE_A4);
                    $page->setFont($font, $font_sz);
                    $line_nr = $page_space;
                
                    /* generate project name */
                    $page->drawText($pg_head, ($limit_width-strlen($pg_head))/4, $page->getHeight()-20);
                    $page->drawText(sizeof($pdf->pages)+1, $limit_width, $page->getHeight()-20);
                    $line_nr += ($font_sz + $line_space)*2;
                }
            }
        
        }
    
        if ($page_nr_max > 0 && $page_nr_max < sizeof($pdf->pages)+1)
            break;

        if ($line_nr > $page_space)
            $pdf->pages[$page_nr] = $page;
    }
    
    $pdf->save($respath."/".$outfile.".pdf");
    clean_path_all($tmp_remote_dir);

    header("Content-type: text/html; charset=utf-8");

    echo "<!DOCTYPE html>";
    echo "<html>";
    echo "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">";
    echo "<link href=\"/img/badsmile.jpg\" rel=\"icon\" type=\"image/jpg\">";
    echo "<body>";
    echo "<div class=\"navigator\">";
    echo "<a name=\"Navigator\"><ul>Navigator</ul></a>";
    echo "<ul>";
    echo "<li><a href=\"starter.py#Motions\" title=\"Motions\">Motions</a></li>";
    echo "<li><a href=\"starter.py#RandomSeq\" title=\"Random Seq\">Random Seq</a></li>";
    echo "<li><a href=\"starter.py#LeaveMessage\" title=\"Leave a Message\">Leave a Message</a></li>";
    echo "</ul>";
    echo "</div>";

    echo "<div class=\"content\">";
    echo "<h2>Welcome, ".getenv("REMOTE_ADDR")."!</h2>";
    echo "<span>".getenv("HTTP_USER_AGENT")."</span><br><br>";

    echo "<div>Source package: ".$_FILES["srcpkg"]["name"]."</div>";
    echo "<div>SrcView: "."<a href=".$respath."/".$outfile.".pdf".">".
        "<span>".$outfile.".pdf"."</span>"."</a>"." generated!</div>";
    echo "<div>Total page: ".sizeof($pdf->pages)."</div>";
    echo "<br><br><div>".$now."</div>";

    echo "</div>";
    echo "</body>";
    echo "</html>";

//    header("Content-type: application/pdf");
//    header("Content-Disposition: attachment;Filename=".$outfile.".pdf");

    } catch (Exception $e) {
       die ('SrcView Error: ' . $e->getMessage());
    }
}

?>
