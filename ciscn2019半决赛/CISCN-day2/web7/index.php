<?php

    class kind
    {
        public static function checkFile(&$page)
        {
            $whitelist = ["source"=>"source.php","click"=>"click.php"];
            if (! isset($page) || !is_string($page)) {
                echo "you can't see it";
                return false;
            }

            if (in_array($page, $whitelist)) {
                return true;
            }

            $_page = mb_substr(
                $page,
                0,
                mb_strpos($page . '?', '?')
            );
            if (in_array($_page, $whitelist)) {
                return true;
            }

            $_page = urldecode($page);
            $_page = mb_substr(
                $_page,
                0,
                mb_strpos($_page . '?', '?')
            );
            if (in_array($_page, $whitelist)) {
                return true;
            }
            echo "you can't see it";
            return false;
        }
    }
	$ischeck = 123;
    if(empty($_REQUEST['file'])) {
        echo "<div style=\"text-align:center;\">";
        echo "<h>A very simple question</h><br>";
        echo "<a href=\"/index.php?file=click.php\">click</a><br>";
        echo "<!--source.php--></div>";
    }
    if (! empty($_REQUEST['file'])
        && is_string($_REQUEST['file'])
        && kind::checkFile($_REQUEST['file'])
    ) {
		
	include $_REQUEST['file'];
        exit;
    } else {
       echo "<center> <h>Look carefully and you will find the answer.</h><br> </center>";
    }
?>
