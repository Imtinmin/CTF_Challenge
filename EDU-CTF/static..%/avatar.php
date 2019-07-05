<?php session_start(); ?>
<?php include("header.php"); ?>
<?php
if(isset($_POST['avatar'])) {
    if(strlen($_POST['avatar']) > 60) die("G___G");
    $av = new Avatar();
    $av->setAV($_POST['avatar']);
    $av->save();
    header("Location: user.php?ud=".$_SESSION['user']);
}
?>
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
    <div class="content">
    <form method="post">
    <h2>Change Avatar</h2>
    <input type="text" name="avatar" placeholder="https://i.imgur.com/..."> &nbsp;<input type="submit">
    </form>
    </div>
    </center>
    </div>
</body>
<?php include("footer.php"); ?>
</html>

