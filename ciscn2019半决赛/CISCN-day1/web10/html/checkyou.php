<?php 
    // 处理用户登录信息
    if (isset($_POST['login'])){
        $user = trim($_POST['user']);
        $passwd = trim($_POST['passwd']);
       header('refresh:2; url=index.php');
       if (($user == '') || ($passwd == '')) {
        echo "用户名或密码不能为空";
        exit;
       }
       else{
        echo "用户名或密码错误";
        }
    }
 ?>