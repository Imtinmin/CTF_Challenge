<?php
require_once('functions.php');
if (!isset($_POST['username']) or !isset($_POST['password'])) {
    include('template/register.html');
    csrf_token();
} else {
    register(addslashes($_POST['username']), addslashes($_POST['password']), $_POST['token']);
}
?>