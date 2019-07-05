<?php 	
header("content-type:text/html;charset=utf-8");
echo <<<_END
	<!DOCTYPE html>
	<html>
	<head>
	<meta charset="UTF-8">
	</head>
	<form action="useri.php" method="post">
	用户名: <input type="text" name="user_name"></br>
	<input type="submit" value="提交">
	</form>
	</html>
_END
?>