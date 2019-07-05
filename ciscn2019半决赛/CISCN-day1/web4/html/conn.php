<?php
$dbhost="127.0.0.1";
$dbname='test';
$dbuser='username';
$dbpass='password';
$dbport=3306;
$mysqli=mysqli_connect($dbhost,$dbuser,$dbpass,$dbname,$dbport);

if (mysqli_connect_errno()){
    echo mysql_conn_error();
}
