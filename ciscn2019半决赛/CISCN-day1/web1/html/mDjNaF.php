<?php
if(';' === preg_replace('/[^\W]+\((?R)?\)/', '', $_GET['code'])) {
	//echo 'hello!cxk';
    eval($_GET['code']);
} else {
    show_source(__FILE__);
}