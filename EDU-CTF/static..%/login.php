<?php include("header.php"); ?>
<?php
    session_start();
    if(isset($_POST['user']) && isset($_POST['pass'])) {
        $user = $_POST['user'];
        $pass = $_POST['pass'];
        if(User::check($user, $pass)) {
            $_SESSION['user'] = User::getIDByName($user);
	    $wrong = false;
            header("Location: index.php");
        } else {
            $wrong = true;
        }
    }

?>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="static/css/style.css">
<link rel="shortcut icon" href="favicon.ico">
<title>TripleSigma</title>
</head>
<body style="background-color:black">
<div class="nav">
    <div class="nav-in">
        <div class="title"> 
            <a href="/">TripleSigma</a>
        </div>
    </div>
</div>
<div class="bd">
    <?php 
        showWrongPass($wrong);
    ?>
    <center>
        <h1 class="font">User Login</h1>
        <form method="post">
            <label for="inp" class="inp">
              <input type="text" name="user" id="inp" placeholder="&nbsp;">
              <span class="label">Username</span>
              <span class="border"></span>
            </label><br>
            <label for="inp" class="inp">
              <input type="password" name="pass" id="inp" placeholder="&nbsp;">
              <span class="label">Password</span>
              <span class="border"></span>
            </label><br><br>
            <input class="btn" type="submit" value="Login">
        </form>
    </center>
    </div>
</body>
<?php include("footer.php"); ?>
</html>
