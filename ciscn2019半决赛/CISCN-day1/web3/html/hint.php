<!DOCTYPE html>
<html>
<head>
	<title>hint!!!!!</title>
</head>
<body>
	<p>I' am hint, but I don't want to show you the secret.<br>
	   However,I can tell you my bro'name is uplllload
	</p>

</body>
</html>
<?php
error_reporting(0);
class Fllllllllag{
	private $flag;

	function __destruct(){
		$flag = file_get_contents('/flag');
		echo $flag;

	}
}

$param = $_GET['do_you_want_it'];

if(isset($param)){
	copy($param, "fuck.bak");
}else{
	exit(0);

}
?>