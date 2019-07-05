<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>can you find the flag?</title>
</head>
<body>
	<?php 
	session_start();
	$password=md5(time());
	$_SESSION['password']=$password;
	header("password:".$password);
	if (isset($_SESSION['id'])) {
		echo "	<form action='upload.php' method='POST' enctype='multipart/form-data'>
		<input type='file' name='file'>
		<button type='submit_file' name='submit_file'>upload</button>
		</form>";
		echo "<form action='logout.php' method='POST'>
		<button type='logout'name='logout'>logout</button>
		</form>";
	}else{

		echo "	<form action='login.php' method='POST'>
		<input type='password' name='password'>
		<button type='submit_passsword' name='submit_password'>login</button>
		</form>";
	}
	if (isset($_GET['login'])) {
		$loginCheck=$_GET['login'];
		if ($loginCheck=="empty") {
			echo "please input the password!";
		}else{
			if ($loginCheck=="errorpassword") {
				echo "You password is wrong!";
			}

		}
	}

	?>
</body>
</html>