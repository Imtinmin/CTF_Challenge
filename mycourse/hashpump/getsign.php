<?php
require_once('function.php');
$secret = "ifPiRcIFHEvmRiUGOIjJLLZbNvpJGe";
if(@$_GET['param']){
echo getsign($secret.$_GET['param']."scan");}
?>

