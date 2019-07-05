<?php session_start(); ?>
<?php include("header.php"); ?>
<?php

if(isset($_POST['title']) && isset($_POST['content'])) {
    if(strlen($_POST['title']) > 250 || strlen($_POST['content']) > 250) die("toooo long");
    if(!isset($_SESSION['user'])) die("wh4t r u doing??");
    if($_POST['action'] === "送出") {
        $art = new Article($_POST['title'], $_POST['content']);
        $art->save();
    } else if($_POST['action'] === "暫存") {
        MyCookie::save($_POST['title'], $_POST['content']);
        header("Location: blog.php");
    }
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
    <h1 style="color:white">Blog</h1>
    <div class="content">

    <?php
        $all = Article::getAll();
        echo $all;
    ?>

    <?php
        if(isset($_COOKIE['e'])) {
            $myck = new MyCookie();
            $r = $myck->restore();
        } else {
	    $r = NULL;
	}
    ?>

    <?php if(isset($_SESSION['user'])): ?>
    <div class="art-form">
        <form method="post" id="article_form">
        <input type="text" name="title" class="in-title" maxlength="250" placeholder="title..." value="<?php print_title($r); ?>" >
            <br>
            <textarea form="article_form" name="content" maxlength="250" placeholder="content..."><?php print_content($r); ?></textarea>
            <br>
            <input type="submit" name="action" value="送出">
            <input type="submit" name="action" value="暫存">
        </form>
    </div>
    <?php endif ?>


    </div>
    </center>
    </div>
</body>
<?php include("footer.php"); ?>
</html>
