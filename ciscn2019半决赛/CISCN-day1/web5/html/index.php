
<html>
 <center><h1>contact administrator</h1></center><br>
 <head></head>
 <body>
  <center>
   <form method="POST" action="index.php">
    <table>
     <tbody>
      <tr>
       <td></td>
       <td><input type="text" name="subject" value="Your Problem" /></td>
      </tr>
      <tr>
       <td></td>
       <td><textarea name="body" cols="80" rows="10">Details</textarea></td>
      </tr>
      <tr>
       <td></td>
       <td><input type="text" name="cback" value="Contact phone or email" /></td>
      </tr>
      <tr>
       <td></td>
       <td><input type="submit" name="action" value="submit" /></td>
      </tr>
     </tbody>
    </table>
   </form>
  </center>
 </body>
</html>

<?php

require "init.php";

function hasTags($text){
	$tags=false;
	$text2=strip_tags($text);
	if($text!==$text2){ $tags=true; }
	return $tags;
}

if(!isset($_POST['subject']) or !isset($_POST['body']) or !isset($_POST['cback'])){
	echo "parameter error";
	exit;
}
$subject=$_POST['subject'];
$body=$_POST['body'];
$cback=$_POST['cback'];
$iscredreq=false;
if ((stripos($subject,"cred")!==false) and (stripos($body,"user")!==false)) $iscredreq=true;
if(hasTags($subject) or hasTags($body)){
	$text = "Oops! Someone is trying to do something nasty...";
} else {
	/* db insert code */
	$mysqli = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
	$sql = $mysqli->prepare("INSERT INTO requests (subject, body, cback) VALUES (?, ?, ?)");
	$sql->bind_param("sss", $subject, $body, $cback);
	$sql->execute();
	$text="Contact request sent.administrator will view it later";
	$sql->close();
	/* db insert code end */
}
        echo $text;
?>
