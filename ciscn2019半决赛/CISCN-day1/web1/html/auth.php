<?php
header("content-type:text/html;charset=utf-8");
        if ($_POST['user_name']=='admin123' and $_POST['user_pwd']=='f4h1l0t0j2g5b1m0a0m0a3d2d0')
                {
                   echo "登录成功，但是flag不在这里哦，试试phpmyadmin";
                }
        else
        {
                echo '密码错误!';
        }
?>