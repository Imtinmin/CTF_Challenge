<?php
require_once('functions.php');
if (!isset($_POST['username']) or !isset($_POST['password'])) {
    if (isset($_GET['loginout'])) {
        loginout();
    }
    if (!isset($_SESSION['login'])) {
        include('template/login.html');
        csrf_token();
    } else {
        Header('Location: /index.php');
    }
} else {
    login(addslashes($_POST['username']), addslashes($_POST['password']), $_POST['token']);
}