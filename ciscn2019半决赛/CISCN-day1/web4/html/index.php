<html>
<head>
    <title>login</title>
    </head>
    <body>
    <center>
    <h1>Login</h1>
    <br><br>
    <form action="./index.php" method="post">
        <p>username: <input type="text" name="username"></p>
        <p>password: <input type="password" name="password"></p>
        <p><input type="submit" name="submit" value="login"></p>
    </form>
</center>
</body>
</html>
<?php
error_reporting(0);
include("conn.php");
echo "game start<br><br>";
$username=$_POST['username'];
$passwd=$_POST['password'];

if(preg_match("/union|benchmark|strcmp|locate|STRCMP|position|md5|mid|sub|concat|and|left|sleep|space|instr|conv|\s|right|cast|locate|limit|reverse|glob|having|match|count|pad|char|hex|regexp|order|group|ascii|information/i",$username))
{
    die('wafed!<br>');
}
if(preg_match("/union|position|strcmp|locate|benchmark|STRCMP|concat|md5|mid|sub|sleep|and|left|cast|space|instr|pad|conv|\s|right|limit|reverse|locate|match|glob|having|count|char|hex|regexp|order|group|ascii|information/i",$passwd))
{
    die('wafed!<br>');
}
else{
    #echo "waf check pass<br><br>";

    $sql="SELECT * FROM user where username = '".$username."' and password = '".$passwd."'";
    #echo $sql."<br><br>";
    $result=$mysqli->query($sql);
    $row = $result->fetch_array();
    $auth=($row['username']);
    if($auth===NULL){
	    die("username or password error");
    }
    if($auth==='admin'){
	echo "login success.<br>Howerver, flag is in /flag"; 
    }
}
?>

