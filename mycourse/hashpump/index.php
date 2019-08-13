<?php
//index.php
error_reporting(0);
require_once('function.php');
require_once('getsign.php');
$filename = $_GET['filename'];
$sign = $_GET['sign'];
$action = urldecode($_GET['action']);

if(strpos($action,'scan') !== False ){
    if(checksign($secret,$action,$filename,$sign)){
    file_put_contents('code.txt',file_get_contents($filename));}
}
if(strpos($action,'read') !== False ){

    if(checksign($secret,$action,$filename,$sign)){
        echo file_get_contents('code.txt');}
}
if(!$action){
highlight_file(__file__);}

?>
