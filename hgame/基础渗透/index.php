<?php
include_once("template/header.php");
if (is_null($_SESSION['user_id'])) {
    header('Location:/login.php');
    exit();
}
$page = array_key_exists('action', $_GET) ? $_GET['action'] : 'message';
require $page .'.php';
include_once("template/footer.php");
?>

