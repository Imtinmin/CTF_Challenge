Administrator backend
<br>
Message from CSO: Our database is running as a user named cxk and have no password protection!!!<br>Also the redis server is useless, please uninstall it
<br>
<img src=http://127.0.0.1/kajndknaknfknaksnjnkankjnijijijqioj92ue.php?url=http://127.0.0.1/logo.png></img>

<?php
$ip=$_SERVER['REMOTE_ADDR'];
if ($ip != '127.0.0.1')
{
	die('this page can only be accessed by 127.0.0.1 <!-- hint xss -->');
}

$x=$_GET["x"];
echo $x;

?>
