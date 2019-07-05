<?php

$flag =file_get_contents("/flag");
$bisskey = "skrskrflag"; // Can't share the key to anyone.

$username = $_POST['username'];
$password = $_POST['password'];

if (!empty($_COOKIE["MyIdentity"])) {
    if (urldecode($username) === "admin123" && urldecode($password) != "admin123") {
        if ($_COOKIE["MyIdentity"] === md5($bisskey . urldecode($username . $password))) {
            echo "Great! You win!\n";
            die ("<!-- Your flag is here ". $flag . "-->");
        }
        else {
            die ("I don't konw what you say!");
        }
    }
    else {
        echo '123';
        die ("I don't konw what you say!");
    }
}

setcookie("hash_key", md5($bisskey . urldecode("admin123" . "admin123")), time() + (60 * 60 * 24 * 7));

if (empty($_COOKIE["source"])) {
    setcookie("source", 0, time() + (60 * 60 * 24 * 7));
}


if ($username !== md5('admin123') || $password !== sha1('admin123')) {
    header('locaton:./admin.php');
} else {
    header('locaton:./admin.php');
}
?>

<!doctype html>
<html itemscope="" itemtype="http://schema.org/SearchResultsPage" lang="zh-ch">
<head>
    <meta charset="UTF-8">
    <title>Hash</title>

    <link rel="stylesheet" type="text/css" href="login.css"/>
    <script type="text/javascript" src="login.js"></script>

</head>

<body>

<div id="login_frame">
    <p id="image_logo"><img src="./small.png" width="200"></p>
    <form name="form1" method="post" action="admin.php">
        Username:
        <input name="username" type="text" id="username"><br>
        Password:
        <input name="password" type="password" id="password"><br><!--爆破是不可能爆破的，我司密码安全等级是最高的-->
        <input name="submit" type="submit" value="submit">
    </form>
</div>

<script type="text/javascript">
         window.onload = function() {
             document.onkeydown = function() {
                 var e = window.event || arguments[0];//banF12
                 if(e.keyCode == 123) {
                     return false;//banCtrl+Shift+I
                 } else if((e.ctrlKey) && (e.shiftKey) && (e.keyCode == 73)) {
                     return false;//banShift+F10
                 } else if((e.shiftKey) && (e.keyCode == 121)){
                     return false;
                 }
             };//banrightclick
             document.oncontextmenu = function() {
                 return false;
             }
         }
 </script>






