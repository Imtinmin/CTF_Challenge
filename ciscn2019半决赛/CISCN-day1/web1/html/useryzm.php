<?php 	
header("content-type:text/html;charset=utf-8");
echo <<<_END
	<!DOCTYPE html>
	<html>
	<head>
	<meta charset="UTF-8">
	</head>
	<form action="yzmi.php" method="post">
	密保手机: 18888888888(四位数验证码已发送！)</br>	
	验证码: <input type="text" name="yzm"></br>
	<input type="submit" value="提交">
	</form>
	<!--我们的验证码是base64的，没想到吧-->
	</html>
_END
?>

