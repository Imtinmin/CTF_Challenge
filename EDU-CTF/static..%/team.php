<?php session_start(); ?>
<?php include("header.php"); ?>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="static/css/style.css">
<link rel="shortcut icon" href="favicon.ico">
<script src="http://code.jquery.com/jquery.min.js"></script>
<title>TripleSigma</title>
</head>
<body style="background-color:black">
<div class="nav">
    <div class="nav-in">
        <div class="title"> 
            <a href="/">TripleSigma</a>
        </div>
        <div class="nav-link">
            <a href="index.php">About</a> &nbsp;&nbsp;|&nbsp;&nbsp;
            <a href="team.php">Team</a> &nbsp;&nbsp;|&nbsp;&nbsp;
            <a href="blog.php">Blog</a>
        </div>
        <div class="login">
        <?php
            if(isset($_SESSION['user'])) {
                echo "<a href='user.php?id=" . $_SESSION['user'] . "'>";
                echo User::getNameByID($_SESSION['user'])."</a> | ";
                echo "<a href='logout.php'>Logout</a>";
            } else {
		echo "<a href='login.php'>Login</a> &nbsp;|&nbsp;&nbsp;";
                echo "<a href='register.php'>Register</a>";
            }
        ?>        
        </div>

    </div>
</div>
<div class="bd">
    <center>
        <h1 style="color:white">Team Member</h1>
        <div class="team">
            <img src="static/img/yvawn.jpg" width="200px"> 
            <span class="team-intro">
                <b>yvawn</b><br>
                Good at: Pwn
            </span>
            <hr>
            <img src="static/img/terryinin.jpg" width="200px">
            <span class="team-intro">
                <b>terryinin</b><br>
                Good at: Reverse
            </span>
            <hr>
            <img src="static/img/ddd.png" width="200px" style="background-color:white; border-radius:3px;">
            <span class="team-intro">
                <b>ddd</b><br>
                Good at: Web
            </span>
            <hr>
            <img src="static/img/meowjui.png" width="200px" style="background-color:white; border-radius:3px;">
            <span class="team-intro">
                <b>meowjui</b><br>
                Good at: Crypto
            </span>
            <hr>
            <img src="static/img/kai6r0.jpg" width="200px" style="border-radius:3px;">
            <span class="team-intro">
                <b>Kai6ro</b><br>
                Good at: Sleep
            </span>
	    <!--
            <a href="joinus.php">You're next!</a>
            -->
        </div>
    </center>
</div>
</body>
<?php include("footer.php"); ?>
</html>
