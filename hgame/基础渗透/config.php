<?php
$DBHOST = "127.0.0.1";
$DBUSER = getenv('DATABASE_USER');
$DBPASS = getenv('DATABASE_PASS');
$DBNAME = "lyb";
$mysqli = new mysqli($DBHOST, $DBUSER, $DBPASS, $DBNAME);
?>