<?php session_start(); ?>
<?php include("header.php"); ?>
<?php
if(!isset($_SESSION['user'])) {
    echo "<script>alert('Please Login!')</script>";
    header("Location: index.php");
    die("");
} else if(Avatar::check()) {
    $uid = $_GET['id'];
    $av = new Avatar();
    $path = $av->setAVFromCookie();
} else {
    $uid = $_GET['id'];
    switch($uid) {
        case 1:
            $img = "kai6r0.jpg";
            break;
        case 2:
            $img = "yvawn.jpg";
            break;
        case 3:
            $img = "terryinin.jpg";
            break;
        case 4:
            $img = "ddd.png";
            break;
        case 5:
            $img = "meowjui.png";
            break;
        default:
            $img = "logo.png";
            break;
    }
    $path = "static/img/" . $img;
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
    <img src="<?php echo $path; ?>"  width="300px"><br>
    <div class="content">
        Name: <?php echo User::getNameByID((int)$uid); ?><br>
    </div>
    <br><br>
    <a href="avatar.php">Set Avatar</a>
    </center>
    </div>
</body>
<?php include("footer.php"); ?>
</html>
