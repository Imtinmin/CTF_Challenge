<?php 
session_start();
if (isset($_SESSION['password'])) {
	if(isset($_POST['submit_password'])){
		if (!empty($_POST['password'])) {
			$password=$_POST['password'];
			if($password==$_SESSION['password']){
				$_SESSION['id']=$password;
				header("Location:index.php");
				exit();
			}else{
				header("Location:index.php?login=errorpassword");
				exit();
			}	
		}else{
			header("Location:index.php?login=empty");
			exit();
		}
	}else{
	header("Location:index.php");
	exit();
	}
}else{
	header("Location:index.php");
	exit();
}
