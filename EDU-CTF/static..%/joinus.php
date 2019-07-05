<?php session_start(); ?>
<?php include("header.php"); ?>
<?php
if(isset($_POST['whoareu'])&&isset($_POST['resume'])) {
    echo shell_exec("date");
    echo "<br>";
    if(strlen($_POST['whoareu']) > 50 || strlen($_POST['resume']) > 450) die("NO! tooooo long!");
    file_put_contents("/tmp/".md5($_SERVER['REMOTE_ADDR']).".txt", base64_encode($_POST['whoareu'] . $_POST['resume']));
    die("OK");
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
    <h2>想加入我們嗎?</h2>
基本資格:<br>
> 須年滿5歲以上<br>
> 無不良嗜好 (例如:麥克雞塊成癮)<br>
<br>
請準備約500字左右的履歷，並附上歷年參賽證明<br>
若有特殊經歷者，斟酌加分 (例如: 國小游泳比賽全校最後一名)<br>
第一階段初試通過會EMAIL通知進入第二階段現場面試<br>
現場面試請穿著正式服裝。<br>
請勿攜帶家中寵物及長輩。<br><br>
<hr>
<br><br>
<form method="post" id="wtf">
<input type="text" name="whoareu" style="width:350px" placeholder="your@email.com"><br>
<textarea style="margin-top: 10px;margin-bottom:10px; border-radius:4px;width:350px;height:150px" placeholder="about you..." form="wtf" name="resume"></textarea><br>
<input type="submit">
</form>
    </div>
    </center>
    </div>
</body>
<?php include("footer.php"); ?>
</html>
